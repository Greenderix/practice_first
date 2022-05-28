import math as m


def main(z):
    res = 35 * (z ** 2 - z - z ** 3) ** 3 - z ** 7 + \
          m.log(11 * z - z ** 3, 2) ** 3 + \
          (12 + 49 * z ** 3) ** 5
    return res
