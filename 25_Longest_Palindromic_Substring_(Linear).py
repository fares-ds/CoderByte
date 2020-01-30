def longest_palindrome(s):
    largest = ''
    if len(s) <= 1:
        return s
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j] == s[i:j][::-1] and len(largest) < len(s[i:j]):
                largest = s[i:j]
    return largest


print(longest_palindrome('ttaaftffftfaafatf'))
print(longest_palindrome('abcba'))
print(longest_palindrome('a'))
