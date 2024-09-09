import pygame
from pygame.locals import *
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2
    player = Player(center_x, center_y)

    dt = 0
    clock = pygame.time.Clock()
    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0,0))
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()

