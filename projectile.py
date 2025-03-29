from time import pthread_getcpuclockid
import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape


class Projectile(CircleShape):
    rotation = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            SHOT_RADIUS,
            2,
        )

    def rotate(self, rotation):
        self.rotation += rotation

    def update(self, dt):
        self.position += self.velocity * dt
