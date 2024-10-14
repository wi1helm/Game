import pygame

from game.fixedGameObject import FixedGameObject

class TextObject(FixedGameObject):

    def __init__(self, text : str, size : int, pos : tuple, textColor: tuple, backgroundColor : tuple = (255,255,255)) -> None:
        self.text = text
        self.size = size
        self.pos = pos
        self.textColor = textColor
        self.backgroundColor = backgroundColor

        font = pygame.font.Font('freesansbold.ttf', self.size)

        self.textObject = font.render(self.text, True, self.textColor, self.backgroundColor)
        self.textRect = self.textObject.get_rect()
        self.textRect.center = self.pos

    def draw(self, screen):

        screen.blit(self.textObject, self.textRect)

