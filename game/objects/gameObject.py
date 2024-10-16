
class GameObject:

    def __init__(self, level: int, pos: tuple) -> None:
        self.level = level
        self.pos = pos

    def getLevel(self):
        return self.level if not self.level < 0 else 0
    