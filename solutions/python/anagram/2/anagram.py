def find_anagrams(word, candidates):
    word_cleaned = word.lower()
    results = []
    for i in range (len(candidates)):
        candidates_cleaned = candidates[i].lower()
        if word == candidates[i] or word.upper() == candidates[i].upper():
            continue
        if sorted(word_cleaned) == sorted(candidates_cleaned):
            results.append(candidates[i])
    return results
