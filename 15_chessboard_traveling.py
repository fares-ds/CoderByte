def chessboard_traveling(string):
    current_position, next_position = [int(string[1]), int(string[3])], [int(string[6]), int(string[8])]

    if current_position[0] > next_position[0] or current_position[1] > next_position[1]:
        return 0

    elif current_position[0] == next_position[0]:
        return next_position[1] - current_position[1]

    elif current_position[1] == next_position[1]:
        return next_position[0] - current_position[0]

    right = next_position[0] - current_position[0]
    up = next_position[1] - current_position[1]
    return right, up


print(chessboard_traveling("(1 1)(3 3)"))
print(chessboard_traveling("(1 1)(1 3)"))
print(chessboard_traveling("(2 2)(4 3)"))
print(chessboard_traveling("(2 2)(4 2)"))
