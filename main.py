import sys
import pygame
from constants import *
from player import Player
from asteroidfield import *
from Bullet import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    Shot.containers = (shot_group, updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = clock.tick(60) /1000
        for obj in updatable_group:
            obj.update(dt)
        for obj in drawable_group:
            obj.draw(screen)
        for obj in asteroids_group:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shot_group:
                if obj.collision(bullet):
                    obj.split()
                    bullet.kill()
        pygame.display.flip()

if __name__=="__main__":
    main()
