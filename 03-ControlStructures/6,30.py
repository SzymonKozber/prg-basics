# Zauważ, że w każdej linii liczby rosną o 7, a wierszy jest 7 (od 1 do 7)
for i in range(1, 8):
    for j in range(7):
        # Obliczamy kolejną liczbę w rzędzie (np. dla i=1: 1, 8, 15...)
        num = i + (j * 7)
        print(f"{num:2d}", end=" ")
    print()  # Przejście do nowej linii po każdym wierszu