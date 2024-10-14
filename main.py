import pygame
from game.game import Game
from game.gameSettings import GameSettings
def main():

    settings = GameSettings((720,300), "Test Game")


    game = Game(settings)
    game.start()


main()
