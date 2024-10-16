import pygame
from game.objects.gameObject import GameObject
class EntityObject(GameObject):

    def __init__(self, level: int, pos: tuple) -> None:
        super().__init__(level, pos)

        self.vel = (0,0)

    def getVelX(self):
        return self.vel[0]

    def getVelY(self):
        return self.vel[1]