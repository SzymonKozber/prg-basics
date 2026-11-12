


def sum_natural(n):
    total = 0
    for num in range (1,n+1):
        total += num
    return total 

print(sum_natural(10))


def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

result = sum_natural(10)
print(result) 

