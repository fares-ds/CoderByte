def powers(n):
    binary = []
    while n > 0:
        binary.append(n % 2)
        n = n // 2
    return [2 ** i for i in range(len(binary)) if binary[i] != 0]


print(powers(11))
