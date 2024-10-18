import pygame

from game.game import Game
from game.gameSettings import GameSettings
from utils.getScreenResolution import get_screen_resolution


def main():


    resolution = get_screen_resolution()

    settings = GameSettings(resolution, "EA Sports", True )


    game = Game(settings)
    game.start()


main()
