matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# Zamiana elementów na głównej przekątnej na 1
for i in range(len(matrix)):
   matrix[i][i] = 1

# Wypisanie zmodyfikowanej tablicy zgodnie ze wzorem
for row in matrix:
   for item in row:
      print(item, end=" ")
   print()