###
# A program that checks what number was entered from the keyboard
# and prints one of the following messages:
# "The number is positive", "The number is negative" or
# "The number is zero"
#
number = int(input("Enter a number: "))
if number > 0:
    print(f'The number {number} is positive')
elif number < 0:
    print(f'The number is negative')
else:
    print(f'The number is zero')
