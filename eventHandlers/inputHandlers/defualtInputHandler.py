import pygame

class InputHandler:

    def __init__(self, call_back_function, entity_object=None) -> None:
        self.call_back = call_back_function
        self.entity = entity_object

    def process_input(self):
        if self.entity is None:
            return

        keys = pygame.key.get_pressed()  # Get the state of all keys

        if keys[pygame.K_w]:  # Move up if 'W' is pressed
            self.call_back((0, -1))
        if keys[pygame.K_s]:  # Move down if 'S' is pressed
            self.call_back((0, 1))
        if keys[pygame.K_d]:  # Move right if 'D' is pressed
            self.call_back((1, 0))
        if keys[pygame.K_a]:  # Move left if 'A' is pressed
            self.call_back((-1, 0))
