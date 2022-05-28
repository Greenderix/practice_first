from datetime import datetime


def change(s):
    s = list(filter(None, s))
    for i in range(len(s)):
        if '/' in s[i]:
            s[i] = s[i].replace('/', '-')
        elif '.' in s[i]:
            s[i] = str(round(float(s[i]), 1))
        elif '+' in s[i]:
            s[i] = s[i].replace(' ', '')
            s[i] = s[i].replace('+7', '')
            s[i] = s[i].replace('-', '')
        elif 'N' == s[i]:
            s[i] = 'Не выполнено'
        else:
            s[i] = 'Выполнено'
    return s

def sorting(s):
    return s[2]
def main(s):
    for i in range(len(s)):
        s[i] = change(s[i])
    s = list(filter(None, s))
    # for i in range(len(s)):
    #     s[i]=sorted([s[2]])
    # s = list(filter(None,s))
    s.sort(key=sorting)
    return s


print(main([['19/05/00', '0.3931', '+7 539 706-7790', 'N'], ['13/05/02', '0.3518', '+7 713 723-0662', 'N'],
            ['26/02/02', '0.1358', '+7 938 899-4719', 'N'], ['19/12/04', '0.8494', '+7 285 685-1548', 'Y']]))
