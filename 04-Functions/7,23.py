def f(password):
    if len(password) < 6:
        return False
    return len(set(password)) == len(password)

# Testy:
print(f("ax15"))     
print(f("book123"))  
print(f("A2water3"))
print(f("qwerty"))   
print(f("aabcdef"))         







def f(password):
    if len(password) < 6:
        return False
    return len(set(password)) == len(password)