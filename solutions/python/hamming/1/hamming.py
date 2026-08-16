def distance(strand_a, strand_b):
    distance = 0
    if len(strand_a) == len(strand_b):
        for char_a,char_b in zip(strand_a,strand_b):
                if char_a != char_b:
                     distance = distance + 1
        return distance
    raise ValueError("Strands must be of equal length.")
