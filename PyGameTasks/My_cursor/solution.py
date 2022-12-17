import pygame
from tools import ImageSprite, load_image


class Cursor(ImageSprite):
    image = load_image('arrow.png')

    def __init__(self, pos, *groups):
        super(Cursor, self).__init__(Cursor.image, pos, *groups)

    def update(self, event) -> None:
        x, y = event.pos
        if pygame.mouse.get_focused():
            self.move(x, y)
        else:
            self.kill()


if __name__ == "__main__":
    group = pygame.sprite.Group()
    win_size = 300, 300

    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(win_size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                group.update(event)
                if not group.sprites() and pygame.mouse.get_focused():
                    Cursor(event.pos, group)

        screen.fill(pygame.Color("white"))
        group.draw(screen)

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()