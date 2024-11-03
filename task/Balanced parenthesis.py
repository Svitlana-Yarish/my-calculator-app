def is_balanced(a):
    count = 0
    for char in a:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


a = is_balanced('(') 
print(a)