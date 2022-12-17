import pygame


def draw_rect(screen, x, y, width, height):
    pygame.draw.rect(screen, pygame.Color('green'), (x, y, width, height))


def handle_event(event):
    if event.type in handlers:
        handlers[event.type](event)


def change_frame():
    for event in pygame.event.get():
        handle_event(event)


def quit():
    global running
    running = False


def tracking(event):
    global pos
    if pinned:
        screen.fill('black')

        x, y = event.pos
        x -= margin[0]
        y -= margin[1]

        draw_rect(screen, x, y, a, a)

        pos = [x, y]


def pin_square(event):
    global pinned, margin
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if pos[0] < x < pos[0] + a and pos[1] < y < pos[1] + a:
            pinned = True
            margin = [x - pos[0], y - pos[1]]
    else:
        pinned = False


handlers = {
    pygame.QUIT: lambda _: quit(),
    pygame.MOUSEMOTION: tracking,
    pygame.MOUSEBUTTONUP: pin_square,
    pygame.MOUSEBUTTONDOWN: pin_square
}


velocity = 10
fps = 50

pos = [0, 0]
margin = []
a = 80

running = True
pinned = False

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Двигалка')
    clock = pygame.time.Clock()
    draw_rect(screen, 0, 0, a, a)

    while running:
        change_frame()
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()