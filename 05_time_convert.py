"""
Time Convert
Have the function TimeConvert(num) take the num parameter being passed and return
the number of hours and minutes the parameter converts to (ie. if num = 63 then
the output should be 1:3). Separate the number of hours and minutes with a colon.
"""


def time_convert(num):
    hours, min = num // 60, num % 60
    return f"{hours}: {min}"


print(time_convert(126))
print(time_convert(220))
