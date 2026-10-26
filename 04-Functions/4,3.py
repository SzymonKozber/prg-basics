###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result
triangle_area_1 = triangle_area(3,4,5)
triangle_area_2 = triangle_area(5,12,13)
triangle_area_3 = triangle_area(7,24,25)
print(f'The area of a triangle with sides 3, 4, 5 is {triangle_area_1}')
print(f'The area of a triangle with sides 5,12,13 is {triangle_area_2}')
print(f'The area of a triangle with sides 7,24,25 is {triangle_area_3}')


