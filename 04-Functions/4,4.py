







def f(number):
    total = 0 
    number = abs(number)
    str_number = str(number)
    for digit in str(number):
        total += int(digit)
    return total
print(f(-1234))