class GameSettings:

    def __init__(self, resolution: tuple, name: str, ) -> None:
        self.resolution = resolution
        self.name = name
    

    def getResolution(self):
        return self.resolution
    
    def getName(self):
        return self.name