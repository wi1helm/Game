import pygame

from game.objects.entityObject import EntityObject
from eventHandlers.inputHandlers.defualtInputHandler import InputHandler
class Player(EntityObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.vel = [0, 0]  # Initial velocity
        self.acc = [0.6, 0.6]
        self.velMax = [1, 1]  # Maximum velocity
        
        self.rect = (100,100)
        self.surface = pygame.Surface((100,100))
        self.surface.fill((22,45,123))

    def update_movement(self, dir):
        self.pos = self.get_x() + dir[0] * self.getMaxVelX() , self.get_y() + dir[1] * self.getMaxVelY()

