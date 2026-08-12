def score(x, y):
    if (x ** 2 + y ** 2) > 100:
        return 0
    if (x ** 2 + y ** 2) <= 100 and (x ** 2 + y ** 2) > 25:
        return 1
    if (x ** 2 + y ** 2) <= 25 and (x ** 2 + y ** 2) > 1:
        return 5
    if (x ** 2 + y ** 2) <= 1 and (x ** 2 + y ** 2) >= 0:
        return 10
