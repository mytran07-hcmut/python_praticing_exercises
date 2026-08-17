def append(list1, list2):
    if not list2:
        return list1
    else:
        for item in list2:
            list1.append(item)
    return list1


def concat(lists):
    results = []
    for item in lists:
        results.extend(item)
    return results


def filter(function, list):
    results = []
    for item in list:
        if function(item) == True:
            results.append(item)
    return results
            


def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    if not list:
        return initial
    result = function(initial, list[0])
    for i in range (1,len(list)):
        result = function(result, list[i])
    return result
        


def foldr(function, list, initial):
    if not list:
        return initial
    result = function(initial,list[-1])
    for i in range((len(list) - 2), -1, -1):
        result = function(result,list[i])
    return result


def reverse(list):
    result = []
    for item in list[::-1]:
        result.append(item)
    return result
