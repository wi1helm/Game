import pygame
# This render requiers each game object to exist with a level. So it knows in what order stuff are rendered.
class Renderer:

    def __init__(self, screen, objects) -> None:
        self.screen = screen
        self.objects = objects()

    def render(self):

        screenObjects = self.objects[0] + self.objects[1]
        
        sortedObjects = sorted(screenObjects, key= lambda obj: obj.get_level())

        for render_object in sortedObjects:
            self.screen.blit(render_object.get_surface(), render_object.get_rect())

        pygame.display.update()