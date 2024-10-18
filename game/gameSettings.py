from xmlrpc.client import Boolean


class GameSettings:

    def __init__(self, resolution: tuple, name: str, fullscreen: Boolean = False ) -> None:
        self.resolution = resolution
        self.name = name
        self.fullscreen = fullscreen
    

    def get_resolution(self):
        return self.resolution
    
    def get_name(self):
        return self.name

    def is_fullscreen(self):
        return self.fullscreen