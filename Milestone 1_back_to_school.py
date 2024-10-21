eq = '4x^2 +4x +    (-8) =  0'

replesed_eq = eq.replace(' ', '')
replesed_eq = replesed_eq.replace('x^2', '').replace('x', '').replace('=0', '')
replesed_eq = replesed_eq.replace('+', ' ')
numbers = replesed_eq.split()
a = int(numbers[0])
b = int(numbers[1])
c = int(eval(numbers[2]))




x1 = (-b + ((b**2 - 4*a*c) ** 0.5)) / (2*a)
x2 = (-b - ((b**2 - 4*a*c) ** 0.5)) / (2*a)

print(a, b, c)
print(x1, x2)
