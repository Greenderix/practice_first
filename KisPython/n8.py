# def main(s: str):
#     res = {}
#     s = s.replace("\n", '')
#     s = s.replace("""\\""", '')
#     s = s.replace(' ', '')
#     s = s.replace('"', '')
#     s = s.replace("begin", '')
#     s = s.replace(";end", '')
#     s = s.replace('.', '')
#     s = s.replace('new', '')
#     s = s.replace('<<', '')
#     s = s.replace('>>', '')
#     for el in s.split(';'):
#         res[el.split('<=')[0]] = el.split('<=')[1]
#
#     return res

def main(s: str):
    res = {}
    s = s.replace("{{", '')
    s = s.replace("loc", '')
    s = s.replace('<%', '')
    s = s.replace('"', "'")
    s = s.replace("%>", '')
    s = s.replace("}}", '')
    # s = s.replace('.', '')
    # s = s.replace('new', '')
    # s = s.replace('<<', '')
    # s = s.replace('>>', '')
    for el in s.split(';'):
        res[el.split('::=')[0]] = el.split('::=')[-1]

    return res
print(main("""<% {{ loc @"quince_919"::= #( -5953 -9777 8807 -9907 ); }}{{loc
@"aeder_130" ::= #(3831 2632); }} {{ loc @"anes_179"::=#( -6651
4021);}} {{loc @"cebe_836" ::= #( -4029 -4302 -4535 5445 ); }} %>"""))
