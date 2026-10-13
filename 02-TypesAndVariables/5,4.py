###
# A program that calculatesand prints amount and its VAT
#
amount = input('Enter amount: ')
amount = float(amount)
vat = amount*0.23
vat = round(vat, 2)
print(f'The amount is {amount} and its VAT is {vat}')
