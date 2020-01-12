def reverse_str(string):
    reversed_str = ''
    for letter in string:
        reversed_str = letter + reversed_str

    return reversed_str


print(reverse_str("I love Paris!"))
print(reverse_str("notebook"))
