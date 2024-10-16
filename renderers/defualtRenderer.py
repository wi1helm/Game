import pygame
# This render requiers each game object to exist with a level. So it knows in what order stuff are rendered.
class Renderer:

    def __init__(self, screen, objects) -> None:
        self.screen = screen
        self.objects = objects()

    def render(self):

        screenObjects = self.objects[0] + self.objects[1]
        
        sortedObjects = sorted(screenObjects, key= lambda obj: obj.getLevel())

        for object in sortedObjects:
            object.draw(self.screen)
        
        pygame.display.update()