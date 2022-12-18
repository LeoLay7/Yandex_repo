import pygame
from tools import load_image
from random import randint


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Bomb, self).__init__(*groups)
        self.image = load_image('bomb.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, 450)
        self.rect.y = randint(0, 450)
        self.boom = False

    def update(self, event):
        x, y = event.pos
        if self.rect.collidepoint(x, y) and not self.boom:
            self.boom = True

            self.image = load_image('boom.png')
            self.rect.x -= 30
            self.rect.y -= 30


if __name__ == '__main__':
    group = pygame.sprite.Group([Bomb() for _ in range(30)])

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill('black')
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                group.update(event)

        screen.fill(pygame.Color('black'))
        group.draw(screen)
        pygame.display.flip()
        clock.tick(50)



