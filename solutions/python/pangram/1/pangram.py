def is_pangram(sentence):
    sentence = sentence.lower()

    letters = {char for char in sentence if char.isalpha()}

    if len(letters) == 26:
        return True
    return False
