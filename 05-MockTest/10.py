def f(sentence):
    ascii_sum = 0
    
    # 1. Liczymy sumę kodów ASCII
    for char in sentence:
        ascii_sum += ord(char)
        
    # 2. Sprawdzamy podzielność przez 3
    if ascii_sum % 3 == 0:
        return True
    else:
        return False