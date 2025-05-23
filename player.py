import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

#Class for player object
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    #method for moving triangle back and forth
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # method for creating triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #method that calls rotate or move method based on user input
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt
        

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    #method for rotating triangle left/right
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    #method to shoot bullets
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        # Use the player's position (self.position) to create the shot
        shot = Shot(self.position.x, self.position.y)
        # Create a velocity vector (0,1) which points down
        # Then rotate it to match the player's rotation
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        # Scale up the velocity to the desired speed
        shot.velocity *= PLAYER_SHOOT_SPEED
