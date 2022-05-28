# def main(x):
#     A = x & 0b111111111
#     B = (x >> 9) & 0b1111111111111111
#     C = (x >> 25) & 0b111111
#     D = (x >> 31) & 0b1
#     res = 0
#     res |= B
#     res |= D << 16
#     res |= C << 17
#     res |= A << 23
#     return res
def main(x):
    A = x & 0b1
    B = (x >> 1) & 0b111111111
    C = (x >> 10) & 0b1111111111
    D = (x >> 12) & 0b11
    F = (x >> 13) & 0b1
    E = (x >> 21) & 0b11111111
    res = 0
    res |= A
    res |= D << 1
    res |= E << 3
    res |= B << 11
    res |= F << 20
    res |= C << 21

    return res

print(hex(main(0xd4194e74)))
