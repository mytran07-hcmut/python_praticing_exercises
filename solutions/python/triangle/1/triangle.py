def isTriangle(sides):
    sum2 = sides[0] + sides[1]
    sum0 = sides[1] + sides[2]
    sum1 = sides[0] + sides[2]
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sum2 >= sides[2] and sum0 > sides[0] and sum1 >= sides[1]:
            return True
    return False
    
def equilateral(sides):
    if isTriangle(sides):
        if sides[0] == sides[1] and sides[1] == sides [2] and sides[0] == sides[2]:
           return True
    return False
    
def isosceles(sides):
    if isTriangle(sides):
        if sides[0] == sides[1] or sides[1] == sides [2] or sides[0] == sides[2]:
           return True
    return False


def scalene(sides):
    if isTriangle(sides):
        if sides[0] != sides[1] and sides[1] != sides [2] and sides[0] != sides[2]:
            return True
    return False
