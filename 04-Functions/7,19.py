def f(number):
    s = str(number)
    total = 0
    for digit in set(s):
        if s.count(digit) > 1:
            total += int(digit) * s.count(digit)
    return total

print(f(1027))      
print(f(230335))     
print(f(513553007))  