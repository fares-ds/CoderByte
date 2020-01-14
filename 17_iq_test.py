def iq_test(numbers):
    # your code here
    lst = ['even' if int(num) % 2 == 0 else 'odd' for num in numbers.split()]

    if lst.count('odd') == 1:
        return lst.index('odd') + 1
    else:
        return lst.index('even') + 1


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))
print(iq_test("2 1 1"))
