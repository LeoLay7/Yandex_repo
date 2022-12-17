import pygame


def get_num():
    try:
        value = float(input())
        if value % 1 == 0:
            return int(value)
        raise ValueError
    except ValueError:
        return None


def chess(screen, side1, side2, count):
    if count % 2 == 0:
        even = True
    else:
        even = False
    if even:
        color = True
    else:
        color = False

    for i in range(side1 // side2):
        for j in range(side1 // side2):
            if color:
                rect_color = '#FFFFFF'
            else:
                rect_color = '#000000'
            pygame.draw.rect(screen, pygame.Color(rect_color), (i * side2,j * side2, side2, side2))
            color = not color
        if even:
            color = not color


if __name__ == '__main__':
    pygame.init()

    print('Сторона поля:')
    a = get_num()
    if a:
        print('Кол-во квадратов:')
        sides = get_num()
        if a:
            screen = pygame.display.set_mode((a, a))
            pygame.display.set_caption('Прямоугольник')

            chess(screen, a, a // sides, sides)

            pygame.display.flip()

            while pygame.event.wait().type != pygame.QUIT:
                pass

            pygame.quit()
        else:
            print('Неправильный формат ввода')
    else:
        print('Неправильный формат ввода')
