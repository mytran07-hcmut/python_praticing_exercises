def is_valid(isbn):
    isbn_cleaned = isbn.replace("-","").lower()
    if len(isbn_cleaned) == 10:
        index = 10
        sum = 0
        for i in range (9):
            if not isbn_cleaned[i].isdigit():
                return False
            sum += int(isbn_cleaned[i]) * index
            index -= 1
        if isbn_cleaned[9] == 'x':
            sum += 10
        elif isbn_cleaned[9].isdigit():
            sum += int(isbn_cleaned[9]) * 1
        else: 
            return False
        if sum % 11 == 0:
            return True
        return False
    return False
    
        
        
            
