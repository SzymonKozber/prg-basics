###
# Conveting the decimal number into a binary one
#
decimal_number = int(input("Enter the number: "))
binary_result = ""
while decimal_number > 0:
    remainder = decimal_number%2
    decimal_number = decimal_number//2
    binary_result = str(remainder) + binary_result
print(binary_result)

