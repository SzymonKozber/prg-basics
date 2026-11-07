def f(dice):
    max_count = 1
    current_count = 1
    most_frequent_digit = int(dice[0])
    
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            current_count = 1
            
        if current_count > max_count:
            max_count = current_count
            most_frequent_digit = int(dice[i])
            
    return most_frequent_digit

print(f("5233165554211"))
print(f("2133"))         