from datetime import timedelta
def add(moment):
    GIGA_SECOND = 10 ** 9
    return moment + timedelta(seconds = GIGA_SECOND)
