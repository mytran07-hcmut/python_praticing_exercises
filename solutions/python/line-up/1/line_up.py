def line_up(name, number):
    converted_number = str(number)
    mapping = {
        "1": "st",
        "2": "nd", 
        "3": "rd",
    }
    if converted_number[-2:] in ['11','12','13']:
        output = name + ", you are the " + converted_number + "th customer we serve today. Thank you!"
    else:
        output = name + ", you are the " + converted_number + mapping.get(converted_number[-1], "th") + " customer we serve today. Thank you!"
    return output
