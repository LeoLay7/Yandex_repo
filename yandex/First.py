def f(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    elif a == 6:
        return 0
    elif a == 12:
        return 0
    return f(a + 1, b) + f(a * 2, b)

print(f(1, 34))