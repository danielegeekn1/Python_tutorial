try:
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError:
    print('divided by zero')
except ValueError:
    print('invalid input')