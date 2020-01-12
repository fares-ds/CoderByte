import math


def distance(one, two):
    return math.sqrt((one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2)


def closet_enemy(str_arr):
    one_position = []
    twos_positions = []

    for i in range(len(str_arr)):
        for j in range(len(str_arr[0])):
            if str_arr[i][j] == '1':
                one_position.append(i)
                one_position.append(j)
            elif str_arr[i][j] == '2':
                twos_positions.append((i, j))
    if twos_positions == []:
        return 0
    
    closest = 999
    closest_coord = []
    for coord in twos_positions:
        dist = distance(one_position, [coord[0], coord[1]])
        if dist < closest:
            closest = dist
            closest_coord = [coord[0], coord[1]]

    if closest_coord[0] == one_position[0]:
        return int(math.fabs(closest_coord[1] - one_position[1]))
    elif closest_coord[1] == one_position[1]:
        return int(math.fabs(closest_coord[0] - one_position[0]))
    elif (closest_coord[0] != one_position[0]) and (closest_coord[1] != one_position[1]):
        return int(math.fabs(closest_coord[1] - one_position[1] - 1))
    else:
        return 0


print(closet_enemy(["000", "100", "200"]))
print(closet_enemy(["000", "120", "000"]))
print(closet_enemy(["0000", "2010", "0000", "2002"]))
print(closet_enemy(["0000", "1000", "0002", "0002"]))
print(closet_enemy(["01000", "00020", "00000", "00002", "02002"]))
# print(distance([1, 0], [2, 2]))
