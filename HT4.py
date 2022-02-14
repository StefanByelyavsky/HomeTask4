a = float(input('первое число:'))
c = input('действие:')
b = float(input('второе число:'))
if c == "/" and b == 0:
    print('на ноль делить нельзя')
elif c == '+' :
    d = a + b
    print(d)
elif c == '-' :
    d = a - b
    print(d)
elif c == '*' :
    d = a * b
    print(d)
elif c == '/' :
    d = a / b
    print(d)
