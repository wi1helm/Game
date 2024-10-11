import pygame

class EventHandler:
    def __init__(self, should_exit_callback) -> None:
        # Here we use dependency injection by passing a callback for setting the exit condition.
        self.should_exit_callback = should_exit_callback

    def process_events(self):
        # This method processes the events and checks if we should quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_exit_callback(True)  # Set exit condition through callback


class Game:

    def __init__(self, resolution: tuple) -> None:
        self.resolution = resolution
        self.running = True  # Track whether the game is running

        self.init()

        self.eventHandler = EventHandler(self.set_running_state)

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.dt = 0

    def set_running_state(self, state: bool):
        self.running = not state

    def start(self):
        while self.running:
            self.eventHandler.process_events()

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            self.dt = self.clock.tick(60) / 1000

        self.end()

    def end(self):
        pygame.quit()
