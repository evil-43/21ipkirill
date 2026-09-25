try:
    num1=input("введите первое число")
    num2=input("введите второе число")
    num1=int(num1)
    num2=int(num2)
    a=num1+num2
    print(a)
except ValueError:
    print('ОШИБКА:нужно вводить целые числа! ')
    
