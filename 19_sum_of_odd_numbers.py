def odd_numbers(n):
    # your code here
    iterations = sum([num for num in range(n + 1)])
    odds = []
    counter = 0
    while len(odds) < iterations:
        if counter % 2 != 0:
            odds.append(counter)
        counter += 1
    return odds


def row_sum_odd_numbers(n):
    return sum(set(odd_numbers(n)).difference(odd_numbers(n - 1)))


print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(4))
