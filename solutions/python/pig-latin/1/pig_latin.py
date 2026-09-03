def translate(text):
    word_list = text.split()
    result = ""
    for i, word in enumerate(word_list):
        if i == 0:
            result = translate_by_word(word)
        else:
            result = result + " " + translate_by_word(word)
    return result
def translate_by_word(word):
    the_vowels = ['a','e','i','o','u']
    start_letters = ""
    for i, char in enumerate(word):
        if char in the_vowels:
            if char == 'u' and word[i-1] == 'q':
                start_letters += char
            else:
                break
        elif char == 'y':
            if i == 0:
                start_letters += char
            else:
                break
        else: 
            start_letters += char
    if word.startswith("xr") or word.startswith("yt") or (word[0] in the_vowels):
        new_text = word + "ay"
    elif word[0] not in the_vowels:
        n = len(start_letters) 
        new_text = word[n:] + start_letters + "ay"
    return new_text