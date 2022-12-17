import pygame.sprite

from sprite_tools import ImageSprite
from image_tools import load_image


class HeroSprite(ImageSprite):
    image = load_image("hero.png")

    def __init__(self, *groups):
        ImageSprite.__init__(self, HeroSprite.image, 0, 0, *groups)
        self.direction = [0, 0]  # hor, vert
        self.speed = 2

    def update(self, *args, **kwargs) -> None:
        self.move(*self.direction)
        if not args:
            return
        event = args[0]
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.direction[0] -= self.speed
            if pressed[pygame.K_RIGHT]:
                self.direction[0] += self.speed
            if pressed[pygame.K_UP]:
                self.direction[1] -= self.speed
            if pressed[pygame.K_DOWN]:
                self.direction[1] += self.speed
        elif event.type == pygame.KEYUP:
            self.direction = [0, 0]


if __name__ == "__main__":
    win_size = 300, 300

    group = pygame.sprite.Group()
    HeroSprite(group)
    pygame.init()
    screen = pygame.display.set_mode(win_size)
    clock = pygame.time.Clock()
    running = True
    while running:
        has_group_updated = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                has_group_updated = True
                group.update(event)
        if not has_group_updated:
            group.update()
        screen.fill(pygame.Color("white"))
        group.draw(screen)

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()