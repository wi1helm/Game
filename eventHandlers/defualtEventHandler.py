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

