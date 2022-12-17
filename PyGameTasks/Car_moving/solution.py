import pygame
from tools import load_image


class Car(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super(Car, self).__init__(*groups)
        self.image = load_image('car2.png')

        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 0
        self.direction = True

    def update(self, *args, **kwargs) -> None:
        if self.rect.x >= 600 - self.rect.width or self.rect.x <= 0:
            self.direction = not self.direction
            self.image = pygame.transform.flip(self.image, True, False)

        if self.direction:
            self.rect.x += 5
        else:
            self.rect.x -= 5


if __name__ == "__main__":

    group = pygame.sprite.Group()
    Car(group)

    pygame.init()
    screen = pygame.display.set_mode((600, 95))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        group.update()

        screen.fill(pygame.Color("white"))
        group.draw(screen)

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()