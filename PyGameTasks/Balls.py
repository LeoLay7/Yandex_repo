import pygame


def draw_circ(screen, center, radius, color):
    pygame.draw.circle(screen, pygame.Color(color), center, radius)


def handle_event(event):
    if event.type in handlers:
        handlers[event.type](event)


def change_frame():
    for event in pygame.event.get():
        handle_event(event)


def quit():
    global running
    running = False


def new_ball(event):
    global squares
    a, b = event.pos
    squares.append([a, b, "left-top"])
    print(event)


def draw(screen):
    global squares
    screen.fill('black')
    for i, square in enumerate(squares):
        x, y, direction = square
        draw_circ(screen, (x, y), 10, 'white')

        if direction == "left-top":
            if x - radius <= 0:
                squares[i][2] = "right-top"

            elif y - radius <= 0:
                squares[i][2] = "left-bot"

            squares[i][0] -= velocity / fps
            squares[i][1] -= velocity / fps

        elif direction == "left-bot":
            if x - radius <= 0:
                squares[i][2] = "right-bot"
            elif y + radius >= 600:
                squares[i][2] = "left-top"

            squares[i][0] -= velocity / fps
            squares[i][1] += velocity / fps

        elif direction == "right-top":
            if x + radius >= 600:
                squares[i][2] = "left-top"
            elif y - radius <= 0:
                squares[i][2] = "right-bot"

            squares[i][0] += velocity / fps
            squares[i][1] -= velocity / fps

        elif direction == "right-bot":
            if x + radius >= 600:
                squares[i][2] = "left-bot"
            elif y + radius >= 600:
                squares[i][2] = "rigth-top"

            squares[i][0] += velocity / fps
            squares[i][1] += velocity / fps


handlers = {
    pygame.QUIT: lambda _: quit(),
    pygame.MOUSEBUTTONUP: new_ball
}

squares = []

radius = 10

velocity = 100
fps = 50

running = True


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Прямоугольник')
    clock = pygame.time.Clock()

    while running:
        change_frame()
        draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()