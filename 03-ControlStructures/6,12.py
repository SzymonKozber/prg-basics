###
# A program that calculates the amount to be paid based on the discount
#
number_of_products_purchased = int(input("Enter the number of items purchased: "))
price = float(input("Enter the pdofuct price: "))
if number_of_products_purchased > 2:
    discount = 0.75 * price
amount_to_pay = number_of_products_purchased * discount
print(f'The amount to pay is {amount_to_pay}')
