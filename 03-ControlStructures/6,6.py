###
# A program that calculates the parking fee based on the number of hours parked.
#
hours_parked = int(input("Enter the number of hours parked: "))
if hours_parked <=2:
    fee = 5
elif hours_parked > 3 and hours_parked <=6:
    fee = 15
elif hours_parked > 6:
    fee = 20
print(f"The parking fee is: ${fee}")