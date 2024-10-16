import pygame

from eventHandlers.defualtEventHandler import EventHandler
from eventHandlers.inputHandlers.defualtInputHandler import InputHandler
from game.entities.player import Player
from renderers.defualtRenderer import Renderer
from game.textObject import TextObject
from game.backGroundObject import BackgroundObject
class Game:

    def __init__(self, game_setting) -> None:
        self.screen = None
        self.worldObjects = None
        self.entityObjects = None
        self.dt = None
        self.clock = None
        self.settings = game_setting
        self.running = True  # Track whether the game is running

        self.init()

        self.eventHandler = EventHandler(self.set_running_state)
        self.renderer = Renderer(self.screen, self.get_game_objects)

        player = Player(3, (500, 500))
        inputHandler = InputHandler(player.update_movement, player)

        self.eventHandler.add_event(inputHandler.process_input)
        self.entityObjects.append(player)
    def init(self):
        pygame.init()
        self.clock = pygame.time.Clock() 
        self.dt = 0 # Frame rate independent physics
        self.init_settings()

        self.entityObjects = []
        self.worldObjects = []
        self.worldObjects.append(TextObject(2,(400,400),"hello",30,(0,20,0)))
        self.worldObjects.append(TextObject(4,(200,200),"Obama",30,(0,20,0)))
        self.worldObjects.append(BackgroundObject(1,(0,0),(178,255,46), self.settings.get_resolution()))



    def set_running_state(self, state: bool):
        self.running = not state

    def get_game_objects(self):
        return self.entityObjects, self.worldObjects

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
        self.screen = pygame.display.set_mode(self.settings.get_resolution())
        pygame.display.set_caption(self.settings.get_name())

