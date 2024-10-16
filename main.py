import pygame
from game.game import Game
from game.gameSettings import GameSettings

def main():

    settings = GameSettings((1280,720), "Game")


    game = Game(settings)
    game.start()


main()
