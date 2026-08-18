def transform(legacy_data):
    result = {}
    for key, value in legacy_data.items():
        for item in value:
            item = item.lower()
            result[item] = key
    return result
        
