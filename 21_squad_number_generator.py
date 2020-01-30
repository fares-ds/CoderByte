def generate_number(squad, n):
    # TODO: complete
    if n not in squad:
        return n
    elif n in squad:
        lowest = []
        for num in squad:
            if n - num >= 0:
                new = int(f"{num}{n - num}")
                if new not in squad and new < 100:
                    lowest.append(new)
        if not lowest or len(str(min(lowest))) > 2:
            return None
        elif len(str(min(lowest))) <= 2:
            return min(lowest)


print(generate_number([1, 2, 3, 4, 6, 9, 10, 15, 69], 11))  # 11
print(generate_number([1, 2, 3, 4, 6, 9, 10, 11, 15, 69], 11))  # 29
print(generate_number([1, 2, 3, 4, 6, 9, 10, 11, 15, 29, 69], 11))  # 38
print(generate_number([1, 2, 3, 4, 6, 9, 10, 11, 15, 29, 38, 47, 56, 65, 69, 74, 83, 92], 11))  # None
