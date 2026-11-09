
def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1

    for _ in range(n - 2):
        temp = a + b  # 1. Obliczamy nową sumę i chowamy do „szufladki” temp
        a = b         # 2. Przesuwamy: stare 'b' ląduje w 'a'
        b = temp      # 3. Nowa suma z temp ląduje w 'b'

    return b
print(f(5))
print(f(9))