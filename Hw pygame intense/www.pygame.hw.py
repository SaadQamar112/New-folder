import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, controls):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.controls = controls
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls[0]]:
            self.rect.y -= self.speed
        if keys[self.controls[1]]:
            self.rect.y += self.speed
        if keys[self.controls[2]]:
            self.rect.x -= self.speed
        if keys[self.controls[3]]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

    def change_color(self):
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.image.fill(self.color)

sprite1 = Sprite((255, 0, 0), 100, 100, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
sprite2 = Sprite((0, 0, 255), 600, 400, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
all_sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.collide_rect(sprite1, sprite2):
        sprite1.change_color()
        sprite2.change_color()

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
