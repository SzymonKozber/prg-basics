###
# A program that anylyses the price of a product and gives a recommendation based
#  on the price.
#
current_price = float(input("Enter the products price: "))
previous_price = float(input("Enter the previous price: "))
if current_price < 0.9*previous_price:
    print("The product is on sale, you should buy it!")
discount = (previous_price - current_price) / previous_price * 100
rounded_discount = round(discount, 0)
print(f"The discount is: {rounded_discount}%")