def f(sentence):
    vowels = "aeiouy"
    count = 0 
    for char in sentence:
        if char in vowels:
            count += 1
    return count

print(f("water"))