import pygame
from eventHandlers.defualtEventHandler import EventHandler
from renderers.defualtRenderer import Renderer
from game.textObject import TextObject
class Game:

    def __init__(self, gameSetting) -> None:
        self.settings = gameSetting
        self.running = True  # Track whether the game is running

        self.init()

        self.eventHandler = EventHandler(self.set_running_state)
        self.renderer = Renderer(self.screen, self.get_game_objects)

    def init(self):
        pygame.init()
        self.clock = pygame.time.Clock() 
        self.dt = 0 # Frame rate independent physics
        self.init_settings()

        self.gameObjects = []
        self.fixedGameObjects = []

        self.fixedGameObjects.append(TextObject("Test", 30, (200,200),(0,20,0)))

    def set_running_state(self, state: bool):
        self.running = not state

    def get_game_objects(self):
        return (self.gameObjects, self.fixedGameObjects)

    def start(self):
        while self.running:
            self.eventHandler.process_events()
            self.renderer.render()
            

            # limits FPS to 60
            self.dt = self.clock.tick(60) / 1000

        self.end()

    def end(self):
        pygame.quit()


    def init_settings(self):
        self.screen = pygame.display.set_mode(self.settings.getResolution())
        pygame.display.set_caption(self.settings.getName())

