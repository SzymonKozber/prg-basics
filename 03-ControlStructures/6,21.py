amount = int(input("Enter the amount in PLN: "))
original_amount = amount

# Obliczamy liczbę monet 5 PLN
coins_5 = amount // 5
amount = amount % 5

# Obliczamy liczbę monet 2 PLN
coins_2 = amount // 2
amount = amount % 2

# Reszta to monety 1 PLN
coins_1 = amount

# Wyświetlamy wyniki
print(f"The amount of PLN {original_amount} in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")
