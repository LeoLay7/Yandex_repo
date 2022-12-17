import pygame


class ImageSprite(pygame.sprite.Sprite):

    def __init__(self, image, x, y, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

