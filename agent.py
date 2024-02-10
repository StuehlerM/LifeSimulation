import pygame
import math
import config
import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.uniform(0, 2 * math.pi)
        self.speed = config.AGENT_SPEED
        self.turn_rate = config.TURN_RATE  # Maximum change in direction per step
        self.health = config.AGENT_MAX_HEALTH
        self.color = config.COLORS[config.Agent.Alive]
        self.health_increment_timer = 0
        self.current_cell = None

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 10)

        # Draw the "point" indicating the direction
        end_x, end_y = self.get_orientation_point()
        pygame.draw.line(win, self.color, (self.x, self.y), (end_x, end_y), 2)

    def live(self, grid, deltaTime):
        if self.health <= 0:
            self.speed = 0
            self.color = config.COLORS[config.Agent.Dead]
            return

        self.sense(grid)

        if self.current_cell == config.CellType.WATER:
            self.drown(deltaTime)
        if self.current_cell == config.CellType.GRASS:
            self.eat(deltaTime)
        else:
            self.speed = config.AGENT_SPEED

        self.move()

    def move(self):
        # Add a small random change to the direction
        self.direction += random.uniform(-self.turn_rate, self.turn_rate)

        # Update position
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

        # Check if agent is outside world boundaries
        self.check_boundaries()

    def sense(self, grid):
        # Calculate the grid cell coordinates
        grid_x = min(int(self.x) // config.CELL_SIZE, config.WORLD_WIDTH)
        grid_y = min(int(self.y) // config.CELL_SIZE, config.WORLD_HEIGHT)
        
        cell = None

        # Check if the coordinates are within the grid
        if 0 <= grid_x < config.GRID_WIDTH and 0 <= grid_y < config.GRID_HEIGHT:
            # Return the value of the grid cell
            cell = grid[grid_x][grid_y]
        
        if cell is not None:
            self.current_cell = cell.cell_type
        else:
            self.current_cell = None

    def drown(self, deltaTime):
        self.speed = config.AGENT_SPEED * config.WATER_SPEED_REDUCTION

        if random.random() < 0.5:
            self.direction += math.pi / 2 * self.turn_rate

        # Increment the timer
        self.health_increment_timer += deltaTime

        # Decrement health every 2-3 seconds, deltaTime is in miliseconds therefore 0.25 equals 2.5 seconds
        if self.health_increment_timer >= 0.25:
            self.health -= config.DROWNING_HEALTH_DECREMENT  # Decrement health
            self.health_increment_timer = 0  # Reset timer
            
    def eat(self, deltaTime):
        if(self.health >= config.AGENT_MAX_HEALTH):
            self.health = config.AGENT_MAX_HEALTH
            return
        
        # Increment the timer
        self.health_increment_timer += deltaTime

        # Increment health every ~2 seconds, deltaTime is in miliseconds therefore 0.2 equals 2 seconds
        if self.health_increment_timer >= 0.2:
            self.health += config.EATING_HEALTH_INCREMENT  # Increment health
            self.health_increment_timer = 0  # Reset timer

    def check_boundaries(self):
        if not (0 <= self.x <= config.WORLD_WIDTH and 0 <= self.y <= config.WORLD_HEIGHT):  # Use config variables
            # Reverse direction
            self.direction += math.pi
            
    def get_orientation_point(self):
        end_x = self.x + 20 * math.cos(self.direction)
        end_y = self.y + 20 * math.sin(self.direction)
        return end_x, end_y