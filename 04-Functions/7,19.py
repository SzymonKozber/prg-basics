
def f(number):
    total = 0
    str_number = str(number)
    
    for digit in set(str_number): 
        
        if str_number.count(digit) > 1: 
            
            total += int(digit) * str_number.count(digit)
            
    return total

print(f(1027)) 
print(f(230335)) 
print(f(513553007)) 




def f(number):
    total = 0
    str_number = str(number)
    for digit in set(str_number):
        if digit.count(set(str_number)) > 1:
            total += int(digit) * set(str(number))
    return total
print(f(230335))

def f(number):
    total = 0
    str_number = str(number)
    for digit in str(number):
        if digit.count(set(str_number)) > 1:
            total +=  int(digit) * set(str_number)
    return total
print(f(230335))