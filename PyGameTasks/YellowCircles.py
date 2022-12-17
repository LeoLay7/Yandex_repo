import pygame


def draw_circ(screen, center, radius, color):
    pygame.draw.circle(screen, pygame.Color(color), center, radius)


def handle_event(event):
    if event.type in handlers:
        handlers[event.type](event)


def change_frame():
    for event in pygame.event.get():
        handle_event(event)


def circ_center(event):
    global center, is_new_circle, radius
    center = event.pos
    is_new_circle = True
    radius = 0


def draw(screen):
    global radius, is_new_circle
    if is_new_circle:
        screen.fill('blue')
        is_new_circle = False
    if center[0] > -1:
        draw_circ(screen, center, radius, 'yellow')
        radius += velocity / fps


def quit():
    global running
    running = False


handlers = {
    pygame.QUIT: lambda _: quit(),
    pygame.MOUSEBUTTONUP: circ_center
}


radius = 0
center = [-1, -1]

velocity = 100
fps = 50

running = True
is_new_circle = False


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Прямоугольник')
    screen.fill('blue')
    clock = pygame.time.Clock()

    while running:
        change_frame()
        draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()