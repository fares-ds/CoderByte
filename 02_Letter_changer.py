"""
Letter Changes
Have the function LetterChanges(str) take the str parameter being passed and
modify it using the following algorithm. Replace every letter in the string
with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally
return this modified string.
"""


def letter_changes(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_str = ''

    for letter in string:
        next_letter = chr(ord(letter) + 1)
        if ord('z') >= ord(letter) >= ord('a') or ord('Z') >= ord(letter) >= ord('A'):
            if next_letter in vowels:
                new_str = new_str + next_letter.upper()
            else:
                new_str = new_str + chr(ord(letter) + 1)
        else:
            new_str = new_str + letter

    return new_str


print(letter_changes('fares'))
