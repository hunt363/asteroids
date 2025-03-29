import pygame
import pygame.display
from asteroid import Asteroid
from asteroidfield import AsteroidField
from projectile import Projectile
from player import Player
from constants import *


def main():
    pygame.init()
    time = pygame.time.Clock()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = updatables
    Player.containers = (updatables, drawables)
    Projectile.containers = (updatables, drawables, projectiles)
    asteroidField = AsteroidField()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    # updatables.add(player)
    # drawables.add(player)
    while True:
        dt: float = time.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        updatables.update(dt=dt)
        for sprite in drawables:
            sprite.draw(screen=screen)
        pygame.display.flip()
        for rock in asteroids:
            if rock.checkCollision(player) == True:
                print("Game Over!")
                exit(0)
            for shot in projectiles:
                if rock.checkCollision(shot):
                    rock.split()
                    shot.kill()


if __name__ == "__main__":
    main()
