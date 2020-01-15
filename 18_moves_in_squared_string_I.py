def vert_mirror(strng):
    # your code
    return '\n'.join([''.join(reversed(word)) for word in strng.split('\n')])


def hor_mirror(strng):
    # your code
    return '\n'.join(reversed(strng.split('\n')))


def oper(fct, s):
    # your code
    return fct(s)


s = "abcd\nefgh\nijkl\nmnop"
print(oper(vert_mirror, s))
print(oper(hor_mirror, s))
