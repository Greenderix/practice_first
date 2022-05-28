s = {
    'ADA': {
        1982: {
            'GOLO': 0,
            'TLA': 1
        },
        2008: {
            'GOLO': {
                'EJS': 2,
                'IOKE': 3,
                'NSIS': 4
            },
            'TLA': 5
        }
    },
    'AWK': {
        1982: {
            'GOLO': 6,
            'TLA': {
                'EJS': 7,
                'IOKE': 8,
                'NSIS': 9
            }
        },
        2008: 10
    },
    'SHELL': 11
}


def main(path):
    s1 = s[path[3]]
    if path[3] == 'ADA':
        s2 = s1[path[4]]
        if path[4] == 1982:
            s3 = s2[path[1]]
            return s3
        elif path[4] == 2008:
            s3 = s2[path[1]]
            if isinstance(s3, int):
                return s3
            return s3[path[0]]
    elif path[3] == 'AWK':
        s2 = s1[path[4]]
        if path[4] == 1982:
            s3 = s2[path[1]]
            if isinstance(s3, int):
                return s3
            return s3[path[0]]
        else:
            return 10
    else:
        return 11

print(main(['NSIS', 'GOLO', 'P4', 'AWK', 2008]))