import struct


def uint32uint16uint32(x, start):
    size = struct.unpack("> I", x[start: start + 4])[0]
    add = struct.unpack("> H", x[start + 4: start + 6])[0]
    a = struct.unpack("> " + "I" * size, x[add: add + 4 * size])
    return list(a)


def uint16uint32uint32(x, start):
    size = struct.unpack("> H", x[start: start + 2])[0]
    add = struct.unpack("> I", x[start + 2: start + 6])[0]
    a = struct.unpack("> " + "I" * size, x[add: add + 4 * size])
    return list(a)


def E(x, start):
    return {
        'E1': struct.unpack("> H", x[start:start + 2])[0],
        'E2': struct.unpack("> H", x[start + 2:start + 4])[0],
        'E3': [struct.unpack("> Q", x[start + 4:start + 12])[0],
               struct.unpack("> Q", x[start + 12:start + 20])[0]],
        'E4': struct.unpack("> H", x[start + 20:start + 22])[0],
        'E5': struct.unpack("> I", x[start + 22:start + 26])[0],
        'E6': struct.unpack("> H", x[start + 26:start + 28])[0],
        'E3': struct.unpack("> I", x[start + 28:start + 32])[0]
    }


def D(x, start):
    return {
        'D1': [struct.unpack("> b", x[start:start + 1])[0],
               struct.unpack("> b", x[start + 1:start + 2])[0],
               struct.unpack("> b", x[start + 2:start + 3])[0],
               struct.unpack("> b", x[start + 3:start + 4])[0]],
        'D2': struct.unpack("> f", x[start + 4:start + 8])[0],
        'D3': struct.unpack("> i", x[start + 8:start + 12])[0]
    }


def addressD(x, start):
    return struct.unpack("> I", x[start:start + 4])[0]


def C(x, start):
    return {
        'C1': str(struct.unpack("> c", x[start:start + 1])[0])[2] +
              str(struct.unpack("> c", x[start + 1:start + 2])[0])[2],
        'C2': struct.unpack("> d", x[start + 2:start + 10])[0],
        'C3': struct.unpack("> B", x[start + 10:start + 11])[0],
        'C4': [struct.unpack("> b", x[start + 11:start + 12])[0],
               struct.unpack("> b", x[start + 12:start + 13])[0],
               struct.unpack("> b", x[start + 13:start + 14])[0]],
        'C5': D(x, addressD(x, start + 14)),
        'C6': struct.unpack("> h", x[start + 18:start + 20])[0]
    }


def addressC(x, start):
    return struct.unpack("> H", x[start:start + 2])[0]


def B(x, start):
    return {
        'B1': struct.unpack("> q", x[start:start + 8])[0],
        'B2': struct.unpack("> b", x[start + 8:start + 9])[0],
        'B3': struct.unpack("> b", x[start + 9:start + 10])[0]
    }


def addressE(x, start):
    return struct.unpack("> H", x[start:start + 2])[0]

# int8 - b
# uint8 - B
# int16 - h
# uint16 - H 16
# int32 - i
# uint32 - I
# int64 - q
# uint64 - Q
def A(x, start):
    return {
        'A1': struct.unpack("> B", x[start:start + 1])[0],
        'A2': [B(x, start + 1), B(x, start + 11),
               B(x, start + 21), B(x, start + 31),
               B(x, start + 41), B(x, start + 51)],
        'A3': C(x, addressC(x, start + 61)),

        'A4': E(x, addressE(x, start + 63)),
        'A5': struct.unpack("> d", x[start + 65:start + 73])[0],
        'A6': struct.unpack("> h", x[start + 73:start + 75])[0],
        'A7': struct.unpack("> q", x[start + 75:start + 83])[0],
        'A8': struct.unpack("> H", x[start + 83:start + 85])[0]

    }


def main(x):
    return E(x, 4)


print(main(b'AHD\xf0\x9b?;\\\xa7\x90\xe33c\xa7]\xb5k\xeb\x8a,E.\x7f\x03\n_Cx'
           b'\xcb\x88\x9b\xf0\x1du\xe0\xdc\xb8\xe6\x16\xa2~\x02\x7f\xd9H\x84t6'
           b'\xf2!\xa6\x05\x9f\x06\x0f\x84\xf5\x1c\x8b\x05Vl\xa30\xe7\x00e\x00'
           b'y\xbf\xd0\x0cX\xfe\x1dYl\xc8\x17"\xcfp\xc2\xf8\xc0\xf2\x82\xdee1Y;j\xbfZ"'
           b'\x8cK\xbeb\xc5ag\xbf\xbdt1\xaf\xd9\xc0\xb0\x88\xc5\x8eN\x00\x00\x00Y\xcf'
           b'\xcd\x84\x8bJSp\xd2-\xe9V\x18\xa6x\xca\xf1\x85\xa9\xa9\xc4\xca\x06\xf2\x11 '
           b'\xcat2B\xfd\xaf`\xab\x1b'))
