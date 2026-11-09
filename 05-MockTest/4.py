def f(card_number):
    masked = card_number[0:2] + "**********" + card_number[12:]
    return masked
print(f("5201928345736214"))



