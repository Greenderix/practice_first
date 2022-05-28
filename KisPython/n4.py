def main(n):
    if n == 0:
        return 0.22
    elif n == 1:
        return 0.20
    elif n >= 2:
        return 1 + main(n - 2) ** 3 - main(n - 1) + main(n - 1) ** 2
