def binary_to_string(binary):

    string = ''
    counter = 0
    while counter < len(binary):
        char = list(reversed(binary[counter: counter + 8]))
        ascii_value = sum([2 ** int(i) for i in range(len(char)) if int(char[i]) == 1])
        counter += 8
        string += chr(ascii_value)
    return string


print(binary_to_string('0100100001100101011011000110110001101111'))
print(binary_to_string(''))
