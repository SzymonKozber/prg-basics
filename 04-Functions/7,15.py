def f(detector):
    current_people = 0
    for action in detector:
        if action == "+":
            current_people += 1
        elif action == "-":
            current_people -= 1
        
        if current_people >= 3:
            return True
            
    return False

print(f("+-+++-+---"))  
print(f("+-+-+-+-"))     
print(f("+-++-+--"))     
print(f("+-++-+-+---"))  