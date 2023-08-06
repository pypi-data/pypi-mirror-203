import os.path
import subprocess
import json
from os import listdir
import pdal
from .bounds import Bounds
from .tile import Tile
from .pipeline_wrapper import PipelineWrapper


class Cloud:
    def __init__(self, filepath, bounds=None):
        self.filepath = filepath
        self.info = self.compute_quick_info()

        if bounds:
            self.bounds = Bounds(bounds[0], bounds[1], bounds[2], bounds[3])
        else:
            bounds_dict = self.info["summary"]["bounds"]
            self.bounds = Bounds(bounds_dict["minx"],
                                 bounds_dict["miny"],
                                 bounds_dict["maxx"],
                                 bounds_dict["maxy"])

    def compute_quick_info(self) -> dict:
        pdal_info = subprocess.run(["pdal", "info", self.filepath, "--summary"],
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

        info = json.loads(pdal_info.stdout.decode())

        return info

    def get_num_points(self) -> int:
        return self.info["summary"]["num_points"]

    def has_ClassFlags_dimension(self) -> bool:
        dimensions = self.info["summary"]["dimensions"]
        return "ClassFlags" in dimensions

    def split(self, tile_size, pipeline, output, buffer=None, n_tiles=None) -> list:
        current_min_x = self.bounds.min_x
        current_min_y = self.bounds.min_y
        current_max_x = current_min_x + tile_size[0] if \
            current_min_x + tile_size[0] <= self.bounds.max_x else self.bounds.max_x
        current_max_y = current_min_y + tile_size[1] if \
            current_min_y + tile_size[1] <= self.bounds.max_y else self.bounds.max_y

        tiles = []

        # This variable will count the number of tiles we cut in the Cloud in the case of a dry run execution
        tiles_created = 0

        while current_max_x <= self.bounds.max_x and current_max_y <= self.bounds.max_y and (tiles_created <= n_tiles if n_tiles else True):
            tile_bounds = Bounds(current_min_x, current_min_y, current_max_x, current_max_y)
            name = str(int(tile_bounds.min_x)) + "_" + str(int(tile_bounds.min_y))
            t = Tile(self, tile_bounds, pipeline, output, buffer, name)

            current_min_x += tile_size[0]
            current_max_x += tile_size[0]

            if current_max_x >= self.bounds.max_x:
                if tile_bounds.max_x < self.bounds.max_x:
                    current_max_x = tile_bounds.max_x + (self.bounds.max_x - tile_bounds.max_x)
                else:
                    current_min_x = self.bounds.min_x
                    current_max_x = current_min_x + tile_size[0]
                    current_min_y += tile_size[1]
                    current_max_y += tile_size[1]

            if current_max_y > self.bounds.max_y:
                if tile_bounds.max_y < self.bounds.max_y:
                    current_max_y = tile_bounds.max_y + (self.bounds.max_y - tile_bounds.max_y)

            tiles.append(t)
            tiles_created += 1

        return tiles

    def load_image_array(self, pipeline):
        wrapper = PipelineWrapper(pipeline)
        wrapper.set_readers_filename(self.filepath)
        p = pdal.Pipeline(json.dumps(wrapper.loaded_pipeline))
        stages = p.stages
        readers = stages.pop(0).pipeline()
        readers.execute()
        return readers.arrays[0]

    def merge(self, output, pipeline):
        wrapper = PipelineWrapper(pipeline)
        outputs = ""
        # Default values according to the pdal writers.las documentation
        compression = 'none'
        minor_version = 2
        dataformat_id = 3

        for f in listdir(output):
            if f.split('.')[1] != "png":
                outputs += '"' + output + '/' + f + '",'

        if outputs != "":
            extension = listdir(output)[0].split('.')[1]
            if extension == 'laz':
                writers_extension = 'las'
                compression = 'laszip'
            else:
                writers_extension = extension

            try:
                minor_version = wrapper.get_writers()[0]['minor_version']
                dataformat_id = wrapper.get_writers()[0]['dataformat_id']
            except KeyError:
                pass

            filename = os.path.basename(self.filepath).split(".")[0]

            merge = '[' + outputs + '{"type": "writers.' + writers_extension + '", "filename":"' + output + '/' + \
                    filename + '.' + extension + '","extra_dims": "all", "compression": "' + compression + '", ' + \
                    '"minor_version": ' + str(minor_version) + ', "dataformat_id": ' + str(dataformat_id) + '}]'

            pdal.Pipeline(merge).execute()
