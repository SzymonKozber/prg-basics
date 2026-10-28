# Definiujemy dwa pierwsze wyrazy ciągu Fibonacciego
a = 0
b = 1

print("Ciąg Fibonacciego:")

# Pętla wykona się 20 razy (dla pierwszych 20 wyrazów)
for i in range(20):
    print(a, end=" ")  # Wypisujemy aktualny wyraz i zostawiamy spację
    
    # Obliczamy kolejny wyraz jako sumę dwóch poprzednich
    # Używamy przypisania wieloaspektowego, aby zaktualizować 'a' oraz 'b'
    a, b = b, a + b