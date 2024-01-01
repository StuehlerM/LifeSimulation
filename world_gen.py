# import noise
import numpy as np
import config
from perlin_noise import PerlinNoise

class Cell:
    def __init__(self, cell_type):
        self.cell_type = cell_type

def generate_world():
    n = PerlinNoise(octaves=config.OCTAVES, seed=1)
    
    # Initialize grid with noise values
    noise = [[n([i / config.SCALE, j / config.SCALE]) 
            for j in range(config.WORLD_HEIGHT)] 
            for i in range(config.WORLD_WIDTH)]
    
    # Initialize grid with noise values
    grid = np.empty((config.WORLD_WIDTH, config.WORLD_HEIGHT), dtype=object)

    # Map noise values to cell types
    for i in range(config.WORLD_WIDTH):
        for j in range(config.WORLD_HEIGHT):
            value = noise[i][j]
            
            if value < -0.05:
                grid[i][j] = Cell(config.CellType.WATER)
            elif -0.05 <= value < 0:
                grid[i][j] = Cell(config.CellType.DESERT)
            elif 0 <= value < 0.05:
                grid[i][j] = Cell(config.CellType.LAND)
            else:
                grid[i][j] = Cell(config.CellType.GRASS)

    return grid