





















def f(x,y):
    count = 0
    for num in range (x,y+1):
        if num < 0 and num % 2 == 0:
            count += 1
    return count

print(f(-7,8))



def f(x,y):
    total = 0
    for digit in range (x,y+1):
        if digit < 0 and digit % 2 == 0:
            total += 1
    return total

print(f(-7,8))