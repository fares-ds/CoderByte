def vowel_square(str_arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(str_arr)):
        for j in range(len(str_arr[0]) - 1):
            if str_arr[i][j] in vowels and str_arr[i][j + 1] in vowels \
                    and str_arr[i + 1][j] in vowels and str_arr[i + 1][j + 1] in vowels:
                return f"{i}-{j}"

    return 'not found'


print(vowel_square(["aqrst", "ukaei", "ffooo"]))
print(vowel_square(["eeei", "ffgi", "kkmo"]))
