###
# A program that prints the message based on the cars speed
#
speed_limit_min = 40
speed_limit_max = 140
car_speed = int(input("Enter the cars speed: "))
if car_speed < 40:
    print("Warning: invalid car speed.")

if car_speed > 140:
    print("Too fast!!! ")