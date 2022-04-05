import numpy as np
from dataclasses import dataclass
from objects.Tile import Tile
from numpy import ndarray


@dataclass
class Grid(Tile):

    __tiles: ndarray[int] = Tile


    def __post_init__(self):
        self.tiles = self.create_grid()


    def create_grid(self, num_tiles_row: int, num_tiles_column: int) -> ndarray: 

        tile_x_pos = 0
        tile_y_pos = 0
        tiles = np.array([])
        
        for tr in range(num_tiles_row):
            for tc in range(num_tiles_column):
                tiles[tr][tc] = Tile(tile_x_pos, tile_y_pos, 20, 20)
                tile_x_pos += 20
            tile_y_pos += 20
        
        return tiles


    @property
    def tiles(self) -> ndarray[Tile]:
        return self.__tiles


    @tiles.setter
    def tiles(self, new_tile: Tile) -> None:
        self.__tile = new_tile