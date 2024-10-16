import pygame

from game.objects.entityObject import EntityObject
from eventHandlers.inputHandlers.defualtInputHandler import InputHandler
class Player(EntityObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.vel = (3,3)
        self.inputHandler = InputHandler(self.update_movement)

        self.rect = (100,100)
        self.surface = pygame.Surface((100,100))
        self.surface.fill("red")

    def update_movement(self, dir):
        print(self.get_x())
        self.pos = self.get_x() + dir[0] * self.getVelX() , self.get_y() + dir[1] * self.getVelY()