def square(number):
    if number >= 1 and number <= 64:
        if number == 1:
           return number
        return square(number - 1) * 2
    raise ValueError("square must be between 1 and 64")


def total():
    sum = 0
    for i in range(1,65):
        sum += square(i)
    return sum
