def f(amount_to_pay):
    coins = 0
    
    # Monet 5 PLN
    coins += amount_to_pay // 5
    amount_to_pay %= 5
    
    # Monet 2 PLN
    coins += amount_to_pay // 2
    amount_to_pay %= 2
    
    # Monet 1 PLN
    coins += amount_to_pay
    
    return coins
print(f(23)) 
print(f(8))  
print(f(2))  
print(f(0))  
