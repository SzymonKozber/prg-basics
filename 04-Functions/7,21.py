def f(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)

print(f(7, 4, 9))   
print(f(2, 12, 8))  



def f(number1, number2, number3):
    if number1 >= number2 and number1 >= number3 and number2 >= number3:
        return number1-number3
    elif number1 >= number2 and number1 >= number3 and number3 >= number2:
        return number1-number2
    elif number2 >= number1 and number2 >= number3 and number1 >= number3:
        return number2 - number3
    elif number2 >= number1 and number2 >= number3 and number3 >= number1:
        return number2 - number1
    elif number3 >= number1 and number3 >= number2 and number1 >= number2:
        return number3 - number2
    elif number3 >= number1 and number3 >= number2 and number2 >= number1:
        return number3 - number1
print(f(7,4,9)) 
print(f(2,12,8)) 