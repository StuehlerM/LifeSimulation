import pygame
import math
import random
import config
import random

class Agent:
    def __init__(self, x, y, ):
        self.x = x
        self.y = y
        self.direction = random.uniform(0, 2 * math.pi)
        self.speed = config.AGENT_SPEED
        self.turn_rate = config.TURN_RATE  # Maximum change in direction per step

    def draw(self, win):
        color = (255, 0, 0)  # Define color as red
        pygame.draw.circle(win, color, (self.x, self.y), 10)

        # Draw the "point" indicating the direction
        end_x, end_y = self.get_orientation_point()
        pygame.draw.line(win, color, (self.x, self.y), (end_x, end_y), 2)
        
    def move(self, cell_value):
        # Add a small random change to the direction
        self.direction += random.uniform(-self.turn_rate, self.turn_rate)
        
        if(cell_value == config.CellType.WATER):
            self.speed = config.AGENT_SPEED * 0.4
            
            if(random.random() < 0.5):
                self.direction += math.pi/2 * self.turn_rate
        else:
            self.speed = config.AGENT_SPEED
        
        
        # Update position
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

        # Check if agent is outside world boundaries
        self.check_boundaries()
        
    def get_orientation_point(self):
        end_x = self.x + 20 * math.cos(self.direction)
        end_y = self.y + 20 * math.sin(self.direction)
        return end_x, end_y

    def check_boundaries(self):
        if not (0 <= self.x <= config.WORLD_WIDTH and 0 <= self.y <= config.WORLD_HEIGHT):  # Use config variables
            # Reverse direction
            self.direction += math.pi

    def sense(self, grid):
        # Calculate the grid cell coordinates
        grid_x = min(int(self.x) // config.CELL_SIZE, config.WORLD_WIDTH)
        grid_y = min(int(self.y) // config.CELL_SIZE, config.WORLD_HEIGHT)

        # Check if the coordinates are within the grid
        if 0 <= grid_x < config.GRID_WIDTH and 0 <= grid_y < config.GRID_HEIGHT:
            # Return the value of the grid cell
            return grid[grid_x][grid_y]
        else:
            # If the agent is outside the grid, return None
            return None