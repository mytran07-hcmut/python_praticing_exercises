def flatten(iterable):
    results = []
    for item in iterable:
        if isinstance(item,(list,tuple)):
            results.extend(flatten(item))
        elif item == None:
            continue
        else:
            results.append(item)
    return results
