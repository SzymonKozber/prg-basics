def hide(card_number):
    if len(card_number) != 16:
        return "Nieprawidłowa długość numeru karty"
    masked = card_number[:2] + "*" * (len(card_number) - 6) + card_number[-4:]
    return masked

card = "5290312400019022"

masked_card = hide(card)

print(masked_card)