is_male = True
is_tall = False
if is_male or is_tall:
    print('You are a male')
elif is_male and not(is_tall):
    print('you are a short male')
else:
    print('you are a female and you are not tall')