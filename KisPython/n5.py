def main(z, y, x):
    n = len(z)
    res = 0
    for i in range(1, n + 1):
        res += (x[n - i] ** 2 + 23 * z[n - i] ** 3 + 61 * y[n - i]) ** 2
    res = res * (69 / 87)
    return res
print(main([-0.83, -0.95, -0.31, 0.88], [0.94, -0.29, 0.75, 0.98], [-0.25, -0.85, -0.47, -0.29]))