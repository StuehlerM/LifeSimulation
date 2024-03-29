from enum import Enum

# Define world size
WORLD_WIDTH = 800
WORLD_HEIGHT = 800

# Define number of agents
NUM_AGENTS = 20
AGENT_SPEED = 1
TURN_RATE = 0.1

# Define grid cell size
CELL_SIZE = 10

# Adjust this value to change the scale of the noise
# Higher values mean more zoomed in and lower more zoomed out
# 50.0 is a good value for the default world size
SCALE = 50.0  

FPS = 60

# Calculate grid size
GRID_WIDTH = WORLD_WIDTH // CELL_SIZE
GRID_HEIGHT = WORLD_HEIGHT // CELL_SIZE

OCTAVES = 3
# PERSISTENCE = 0.5
# LACUNARITY = 2.0

RENDER_GRID = False

WATER_SPEED_REDUCTION = 0.4
DROWNING_HEALTH_DECREMENT = 10
EATING_HEALTH_INCREMENT = 10
AGENT_MAX_HEALTH = 100

# Define cell types
class CellType(Enum):
    WATER = 0
    DESERT = 1
    LAND = 2
    GRASS = 3
    
class Agent(Enum):
    Alive = 1
    Dead = 0

# Define colors
COLORS = {
    CellType.WATER: (0, 0, 255),   # Blue
    CellType.DESERT: (205, 133, 63),  # Brownish Yellow
    CellType.LAND: (0, 195, 0),  # Green
    CellType.GRASS: (0, 128, 0),  # Dark Green
    Agent.Alive: (255, 0, 0), # Red
    Agent.Dead: (0, 0, 0)  # Black
}