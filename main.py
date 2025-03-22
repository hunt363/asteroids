from curses import COLOR_BLACK
import pygame
import pygame.display
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=COLOR_BLACK)
        pygame.display.flip()


if __name__ == "__main__":
    main()
