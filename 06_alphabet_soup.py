"""
Alphabet Soup
Have the function AlphabetSoup(str) take the str string parameter being passed and
return the string with the letters in alphabetical order (ie. hello becomes ehllo).
Assume numbers and punctuation symbols will not be included in the string.
"""


def alpha_soup(string):
    return ''.join(sorted(list(string)))


print(alpha_soup("coderbyte"))
print(alpha_soup('fares'))
