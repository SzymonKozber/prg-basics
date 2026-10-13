###
# A program that allows you to enter the product pricae and discount
# and prints the product price discount discounted product price and 
# the amount of discount.
#
product_price = float(input('Enter product price: '))
discount = float(input('Enter discount: '))
discounted_price = product_price - (product_price * (discount / 100))
difference = product_price - discounted_price
amount_of_discount = round(difference, 2)
print(f'The product price is {product_price}')
print(f'The discount is {discount}')
print(f'The discounted product price is {discounted_price}')
print(f'The amount of discount is {amount_of_discount}')