def is_armstrong_number(number):
    sum = 0
    str_num = str(number)
    for i in range (len(str_num)):
        sum += (int(str_num[i]) ** len(str_num))
    if sum == number:
        return True
    return False
