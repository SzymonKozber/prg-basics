n = int(input("Podaj ile pierwszych liczb pierwszych wypisać: "))

count = 0  # Licznik znalezionych liczb pierwszych
number = 2  # Liczba, którą sprawdzamy

while count < n:
    # Sprawdzamy, czy 'number' jest liczbą pierwszą
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
        count += 1

    number += 1