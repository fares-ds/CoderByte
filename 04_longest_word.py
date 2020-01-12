"""
Longest Word
Have the function LongestWord(sen) take the sen parameter being passed and return
the largest word in the string. If there are two or more words that are the same
length, return the first word from the string with that length. Ignore punctuation
and assume sen will not be empty.
"""


def longest_word(sen):
    sen_to_lst = sen.split(' ')
    word_len = dict()

    for word in sen_to_lst:
        counter = 0
        for letter in word:
            if ord('z') >= ord(letter) >= ord('a') or ord('Z') >= ord(letter) >= ord('A'):
                counter += 1
        word_len[word] = counter

    big_word = ''
    counter = 0

    for key, item in word_len.items():
        if item > counter:
            counter = item
            big_word = key

    return big_word


print(longest_word('I love Paris, more than NewYork'))
print(longest_word("fun&!! time"))
