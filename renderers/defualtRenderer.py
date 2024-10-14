import pygame

class Renderer:

    def __init__(self, screen, objects) -> None:
        self.screen = screen
        self.objects = objects()

    def render(self):

        fixedGameObjects = self.objects[1] # Take the fixed game object list from the object tuple        
        gameObjects = self.objects[0] # Take the game object list from the object tuple


        for fixed_object in fixedGameObjects:
            fixed_object.draw(self.screen)

        for object in gameObjects:
            object.draw(self.screen)

        pygame.display.update()