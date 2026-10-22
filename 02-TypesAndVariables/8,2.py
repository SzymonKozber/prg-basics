###
# Calculation of circle area and circumference 
#

# determine radius and PI values
radius = float(input('Enter radius: '))
PI = 3.14159    
# calculate area 
area = PI * radius ** 2
area = round(area, 2)
# calculate circumference 
circumference = 2 * PI * radius
circumference = round(circumference, 2)
# print results
print(f'Area: {area}')
print(f'Circumference: {circumference}')
