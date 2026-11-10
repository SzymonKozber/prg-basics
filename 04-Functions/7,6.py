def hide(card_number):
    masked_number = card_number[:2] + "**********" + card_number [-4:]
    return masked_number
print(hide('12344221231231'))