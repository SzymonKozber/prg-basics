


def f(binary_number):
    for char in binary_number:
        if char not in ['1', '0']:
            return False
    return True


print(f("101101"))      
print(f("1311a10100"))  

