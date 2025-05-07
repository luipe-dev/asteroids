import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group() #group for all objects that can be updated
    drawable = pygame.sprite.Group() # group for all objects than can be drawn
    Player.containers = (updatable, drawable)

    # Initiate Player Object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) # move player's position
        screen.fill("black") # generate black screen
        for obj in drawable:
            obj.draw(screen) # render the player on the screen
        pygame.display.flip() #flip screen

        dt = clock.tick(60) / 1000 #limit framerate to 60 FPS


if __name__ == "__main__":
    main()