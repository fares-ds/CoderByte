import ast


def find_intersection(str_arr):
    lst_1 = set(ast.literal_eval(str_arr[0]))
    lst_2 = set(ast.literal_eval(str_arr[1]))
    intersect = lst_1.intersection(lst_2)

    if intersect == set():
        return 'false'
    else:
        string = str(intersect)
        string = string.replace('{', '')
        string = string.replace(' ', '')
        string = string.replace('}', '')
        return string


print(find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
print(find_intersection(["2, 3, 4", "3"]))
