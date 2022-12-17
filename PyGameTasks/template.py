import pygame


def handle_event(event):
    if event.type in handlers:
        handlers[event.type](event)


def change_frame():
    for event in pygame.event.get():
        handle_event(event)


def quit():
    global running
    running = False


handlers = {
    pygame.QUIT: lambda _: quit(),
}


velocity = 10
fps = 50

running = True


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Прямоугольник')
    clock = pygame.time.Clock()

    while running:
        change_frame()
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()