def f(name):
    words = name.split()
    return "".join(word[0] for word in words)

print(f("Internet of Things"))    
print(f("For Your Information"))   
print(f("Python"))                 



def f(name):
    result =""
    words = name.split()
    for word in words:
        result += word[0]
    return result
print(f("Internet of Things"))    
print(f("For Your Information"))   
print(f("Python"))                 



def acronym(name):
    result = ""
    for word in name.split():
        result += word[0]
    return result

print(acronym("Internet of Things"))    # IoT
print(acronym("For Your Information"))  # FYI
print(acronym("Python"))                # P