def kaprekars_constant(num):
    counter = 0
    while True:
        str_num = str(num)
        if len(str_num) < 4:
            str_num = str_num + '0' * (4 - len(str_num))

        digit_str = list(str_num)

        bigger = list(sorted(digit_str, reverse=True))
        smaller = list(sorted(digit_str))

        bigger = int(''.join(bigger))
        smaller = int(''.join(smaller))

        diff = bigger - smaller

        if diff == int(''.join(digit_str)):
            break
        num = diff
        counter += 1
        print(diff)
    return counter


print(kaprekars_constant(3524))
