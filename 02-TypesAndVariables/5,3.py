###
# A program that calculates the volume
# and surdface area of a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input("Enter the length of side a: ")
b = input("Enter the length of side b: ")
c = input("Enter the length of side c: ")
a = int(a)
b = int(b)
c= int(c)
surface_area = 2*a*b + 2*a*c + 2*b*c
volume = a*b*c
print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, and {c} is {surface_area}')