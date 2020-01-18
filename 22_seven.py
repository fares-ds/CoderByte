def seven(m):
    # your code
    lst = []
    nbr = str(m)
    if m == 0:
        return 0, 0
    while len(nbr) > 2:
        new = int(nbr[:-1]) - 2 * int(nbr[-1])
        if new < 0:
            break
        lst.append(new)
        nbr = str(new)
    if not lst:
        return 1
    else:
        if len(str(lst[-1])) > 2:
            last = str(lst[-1])
            return int(last[:-1]) - 2 * int(last[-1]), len(lst) + 1
        else:
            return lst[-1], len(lst)


print(seven(371))
print(seven(1603))
print(seven(483))
print(seven(1223))
