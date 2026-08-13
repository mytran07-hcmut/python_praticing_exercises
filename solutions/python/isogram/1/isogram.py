def is_isogram(phrase):
    phrase = phrase.lower()
    letters = [char for char in phrase if char.isalpha()]
    if len(letters) == len(set(letters)):
        return True
    return False