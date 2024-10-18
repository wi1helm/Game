import pygame
from pygame.display import update

from game.objects.entityObject import EntityObject
from eventHandlers.inputHandlers.defualtInputHandler import InputHandler
class Player(EntityObject):

    def __init__(self, level: int, pos: tuple):
        super().__init__(level, pos)
        self.vel = [0, 0]  # Initial velocity
        self.acc = [0.3, 0.3]
        self.velMax = [4, 4]  # Maximum velocity
        
        self.rect = (100,100)
        self.surface = pygame.Surface((100,100))
        self.surface.fill((22,45,123))

    def update_movement(self, dir):
        self.pos = self.get_x() + dir[0] * self.getMaxVelX() , self.get_y() + dir[1] * self.getMaxVelY()

    def update_movement_vel(self, dir):
        self.pos = self.get_x() + dir[0] * self.getVelX(), self.get_y() + dir[1] * self.getVelY()

    def update_movement_acc(self, dir):
        if dir == (0,0):
            self.vel = (0,0)
            return
        print(self.vel)
        if self.getVelX() >= self.getMaxVelX() and self.getVelY() >= self.getMaxVelY():
            self.update_movement(dir)
        else:
            self.vel = self.getVelX() + self.getAccX(), self.getVelY() + self.getAccY()
            self.update_movement_vel(dir)

