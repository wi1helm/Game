class GameSettings:

    def __init__(self, resolution: tuple, name: str, ) -> None:
        self.resolution = resolution
        self.name = name
    

    def get_resolution(self):
        return self.resolution
    
    def get_name(self):
        return self.name