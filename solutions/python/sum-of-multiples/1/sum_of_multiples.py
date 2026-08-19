def sum_of_multiples(limit, multiples):
    multiples_list = set()
    for base_value in multiples:
        if base_value > 0:
            multiples_list.update(range(base_value, limit, base_value))
    return sum(multiples_list)
            
            
