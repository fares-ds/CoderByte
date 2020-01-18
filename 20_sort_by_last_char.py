def last(x):
    # your code here
    lst = x.split(' ')
    reverse_lst = [''.join(list(reversed(lst[i]))) for i in range(len(lst))]

    lst = sorted(reverse_lst)
    sorted_lst = [''.join(list(reversed(lst[i]))) for i in range(len(lst))]

    return sorted_lst


print(last("man i need a taxi up to ubud")) # "a", "need", "ubud", "i", "taxi", "man", "to", "up"
