is_male = True
is_tall = False
if is_male or is_tall:
    print('You are a male')
elif is_male and not(is_tall):
    print('you are a short male')
else:
    print('you are a female and you are not tall')

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(4, 6, 9))
