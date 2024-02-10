# Project Overview

This project involves creating a simulated world with agents that can interact with their environment. The project can be broken down into the following steps:

## 1. World Creation

- Create a basic world with different tiles.
- Represent the world as a 2D grid where each cell represents a tile.
- Each tile can have properties like type (water, land, grass, wasteland), food availability etc.

## 2. Agent Creation

- Create simple agents with basic rules.
- Each agent can have properties like position, health, energy etc.
- Agents should have methods for actions like move, eat, mate, die.

## 3. Sensory Input

- Improve agents by adding sensory input.
- Agents should be able to perceive their surroundings (nearby tiles) and make decisions based on that.

## 4. Learning with AI

- Introduce learning capabilities using AI.
- Use reinforcement learning where agents learn to perform actions based on reward/punishment.
- PyTorch will be useful here.

## 5. Threats and Predators

- Introduce threats like predators.
- This will add another layer of complexity and make the simulation more realistic.

## 6. Genetic Diversity

- Introduce genetic diversity.
- Agents can inherit traits from their parents with some mutations.
- This can lead to evolution over generations.

## 7. Self-Improving AI

- Try to implement a self-improving AI.
- This is a complex task and might involve advanced AI concepts like meta-learning.


## How to Run

Before running the project, make sure you have Python installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).

Next, install the required packages. You can do this by running the following commands in your terminal:

```bash
pip install pygame
pip install numpy
pip install matplotlib
pip install perlin-noise
pip install Enum