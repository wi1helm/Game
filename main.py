import pygame
from game.game import Game
from game.gameSettings import GameSettings

def main():

    settings = GameSettings((500,400), "EA Sports")


    game = Game(settings)
    game.start()


main()
