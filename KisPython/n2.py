import math as m


def main(y):
    if y < 85:
        return 22 * (y ** 5) - y ** 2
    elif 85 <= y < 183:
        return ((y ** 3) / 64) ** 2 + (m.floor(y)) ** 6
    elif y >= 183:
        return 38 * (y ** 7) - (33 * (y ** 3) + 82) ** 3 - y


print(main(1))
