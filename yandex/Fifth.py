import pygame


def get_num():
    try:
        value = float(input())
        if value.is_integer():
            return int(value)
        raise ValueError
    except ValueError:
        return None


def draw_circ(screen, center, radius, color, width):
    pygame.draw.circle(screen, pygame.Color(color), center, radius, width)


def make_epileptic(screen, center, radius, width, n):
    color = '#FF0000'

    for i in range(n + 1):
        draw_circ(screen, center, radius + i * width, color, width)
        color = switch_color(color)


def switch_color(color: str):
    if color.startswith('#FF'):
        return '#00FF00'
    elif color.endswith('FF'):
        return '#FF0000'
    else:
        return '#0000FF'


if __name__ == '__main__':
    pygame.init()

    print('ширина:')
    width = get_num()
    if width:
        print("кол-во кругов")
        n = get_num()
        if n:
            screen = pygame.display.set_mode((n * width * 2, n * width * 2))

            a = n * width

            make_epileptic(screen, (a, a), width, width, n - 1)

            pygame.display.flip()

            while pygame.event.wait().type != pygame.QUIT:
                pass

            pygame.quit()
        else:
            print('Неправильный формат ввода')
    else:
        print('Неправильный формат ввода')




