###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# entering temperature in degrees Celsius
celsius = float(input('Enter temperature in degrees Celsius: '))
# converting temperature to degrees Fahrenheit
fahrenheit = (celsius * 9/5) + 32
# converting temperature to Kelvin
kelvin = celsius + 273.15
# printing results
print(f'Temperature in degrees Fahrenheit: {fahrenheit}')
print(f'Temperature in Kelvin: {kelvin}')