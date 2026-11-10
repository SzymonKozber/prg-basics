


def sum_digits(number):
    number = abs(number)
    string_number = str(number)
    running_total = 0
    for digit in str(number):
        running_total += int(digit)
    return running_total

input_number = int(input("Enter the number: "))
sum_value = sum_digits(input_number)
print(f"The sum of digits in the number {input_number} is {sum_value}")




