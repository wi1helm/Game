import pygame
from game.objects.gameObject import GameObject
class EntityObject(GameObject):

    def __init__(self, level: int, pos: tuple) -> None:
        super().__init__(level, pos)
        self.acc = (0,0)
        self.vel = (0,0)
        self.velMax = (0,0)
    def getVelX(self):
        return self.vel[0]

    def getVelY(self):
        return self.vel[1]

    def getMaxVelX(self):
        return self.velMax[0]

    def getMaxVelY(self):
        return self.velMax[1]

    def getAccX(self):
        return self.acc[0]

    def getAccY(self):
        return self.acc[1]