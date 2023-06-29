import random
import math

class Solution:
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        # Generate random angle in radians
        angle = random.uniform(0, 2*math.pi)
        # Generate random radius between 0 and the circle's radius
        rand_radius = math.sqrt(random.uniform(0, 1)) * self.radius
        # Calculate the coordinates of the point
        x = self.x_center + rand_radius * math.cos(angle)
        y = self.y_center + rand_radius * math.sin(angle)
        return [x, y]
