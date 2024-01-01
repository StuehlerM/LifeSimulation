import pygame
from world_gen import generate_world
from agent import Agent
import config
import random
import noise

# Initialize Pygame
pygame.init()

# Set up display variables
win = pygame.display.set_mode((config.WORLD_WIDTH, config.WORLD_HEIGHT))

# Generate world
world = generate_world()

# Create agent
agents = [Agent(random.randint(0, config.WORLD_WIDTH), random.randint(0, config.WORLD_HEIGHT)) for _ in range(config.NUM_AGENTS)]  # Use list comprehension

# Create a surface for the world
world_surface = pygame.Surface((config.WORLD_WIDTH * config.CELL_SIZE, config.WORLD_HEIGHT * config.CELL_SIZE))

# Draw world onto surface
for i in range(config.WORLD_WIDTH):
    for j in range(config.WORLD_HEIGHT):
        # Get cell type
        cell_type = world[i][j].cell_type

        # Get color for cell type
        color = config.COLORS[cell_type]

        # Draw cell onto world surface
        pygame.draw.rect(world_surface, color, pygame.Rect(i * config.CELL_SIZE, j * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE))

if(config.RENDER_GRID):
    # Draw grid lines
    for i in range(config.WORLD_WIDTH):
        pygame.draw.line(world_surface, (255, 255, 255), (i * config.CELL_SIZE, 0), (i * config.CELL_SIZE, config.WORLD_HEIGHT * config.CELL_SIZE))
    for j in range(config.WORLD_HEIGHT):
        pygame.draw.line(world_surface, (255, 255, 255), (0, j * config.CELL_SIZE), (config.WORLD_WIDTH * config.CELL_SIZE, j * config.CELL_SIZE))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw world surface onto screen
    win.blit(world_surface, (0, 0))

    # Game logic goes here
        
    # Update and draw each agent
    for agent in agents:
        cell = agent.sense(world)
        
        if cell is not None:
            cell_value = cell.cell_type
        else:
            cell_value = config.CellType.LAND

        agent.move(cell_value)
        agent.draw(win)

    # Draw/update screen
    pygame.display.flip()

    # Cap the frame rate (optional)
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()