def is_paired(input_string):
    stack = []
    special_chars = {')':'(', ']':'[', '}':'{'}
    for char in input_string:
        if char in special_chars.values():
            stack.append(char)
        elif char in special_chars.keys():
            if not stack or stack[-1] != special_chars[char]:
                return False
            stack.pop()
    return len(stack) == 0
