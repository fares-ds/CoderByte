import re


def question_mark(string):
    string = re.sub(r'[a-zA-Z]', '', string)
    numbers = re.sub(r'[?]', '', string)

    previous_number = 0
    question_num = 0

    for letter in string:
        if letter.isalnum():
            if letter.isnumeric() and (int(letter) + previous_number == 10) and question_num == 3:
                return True
            else:
                previous_number = int(letter)
            question_num = 0

        if letter == "?":
            question_num += 1
    return False


print(question_mark("arrb6???4xxbl5???eee5"))
print(question_mark("aa6?9"))
print(question_mark("acc?7??sss?3rr1??????5"))
