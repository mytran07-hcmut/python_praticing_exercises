def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factor = []
    aliquot_sum = 0
    if number > 0:
        for i in range (1, number + 1):
            if number % i == 0:
                factor.append(i)
        for i in range(1, len(factor)):
            aliquot_sum += factor[i-1]
        if aliquot_sum == number:
            return "perfect"
        if aliquot_sum > number:
            return "abundant"
        if aliquot_sum < number:
            return "deficient"
    raise ValueError("Classification is only possible for positive integers.")
        
