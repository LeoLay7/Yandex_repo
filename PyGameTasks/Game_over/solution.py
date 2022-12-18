import pygame
from tools import load_image


class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(ImageSprite, self).__init__(*groups)
        self.image = load_image('game_over_image.png')
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self, fps, speed) -> None:
        if self.rect.x < 0:
            self.rect.x += speed / fps


if __name__ == "__main__":
    group = pygame.sprite.Group()

    group.add(ImageSprite())

    pygame.init()
    screen = pygame.display.set_mode((600, 300))
    clock = pygame.time.Clock()
    fps = 50
    speed = 200
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.update(fps, speed)

        screen.fill('white')
        group.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
