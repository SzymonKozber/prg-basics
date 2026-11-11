



def f(detector):
    current = 0
    for action in detector:
        if action == "+":
            current += 1
        elif action == "-":
            current -= 1
        if current >= 3:
            return True
    return False  
print(f("+-+++-+---"))
print(f("+-+-+-+-"))     
print(f("+-++-+--"))     
print(f("+-++-+-+---"))  
