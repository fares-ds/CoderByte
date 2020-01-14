def in_array(array1, array2):
    # your code
    item_lst = []
    for item1 in array1:
        for item2 in array2:
            if item1 in item2:
                item_lst.append(item1)
    return list(set(item_lst))


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1, a2))
