import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Initiate Player Object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)

    dt = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # generate black screen
        player.draw(screen) # render the player on the screen
        pygame.display.flip() #flip screen

        dt = clock.tick(60) / 1000 #limit framerate to 60 FPS


if __name__ == "__main__":
    main()