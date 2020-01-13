def kaprekars_constant(num):
    digit_str = list(str(num))

    bigger = list(sorted(digit_str, reverse=True))
    smaller = list(sorted(digit_str))

    bigger = int(''.join(bigger))
    smaller = int(''.join(smaller))

    return bigger - smaller


print(kaprekars_constant(3524))
