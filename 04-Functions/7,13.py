def f(n):
    return "".join(str(i) for i in range(1, n + 1))

# Testy:
print(f(11)) # "1234567891011"
print(f(4))  # "1234"