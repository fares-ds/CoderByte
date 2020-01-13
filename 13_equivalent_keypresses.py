def equivalent_keypress(str_arr):
    str_1 = list(reversed(str_arr[0].split(',')))
    str_2 = list(reversed(str_arr[1].split(',')))

    i = 0
    new_str_1 = []
    while i <= len(str_1) - 1:
        if str_1[i] != '-B':
            new_str_1.append(str_1[i])
            i += 1
        else:
            i += 2

    i = 0
    new_str_2 = []
    while i <= len(str_2) - 1:
        if str_2[i] != '-B':
            new_str_2.append(str_2[i])
            i += 1
        else:
            i += 2

    if new_str_1 == new_str_2:
        return 'true'
    else:
        return 'false'

# true
print(equivalent_keypress(["a,b,c,d", "a,b,c,d,-B,d"]))
# false
print(equivalent_keypress(["c,a,r,d", "c,a,-B,r,d"]))
# true
print(equivalent_keypress(["q,w,e,r,t,y", "-B,-B,q,w,w,-B,e,r,t,y"]))
# true
print(equivalent_keypress(["p,o,i,n,-B,t", "-B,p,o,i,t"]))
# true
print(equivalent_keypress(["u,m,b,r,r,-B,e,l,l,a", "u,m,b,b,-B,r,e,l,l,a"]))
