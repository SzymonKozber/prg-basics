





























def counting_letter_e(string):
    count = 0  
    for letter in string:
        if letter == 'e':
            count += 1
    return count 

print(counting_letter_e('You never get a second chance to make a first impression'))
