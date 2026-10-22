###
# A program that checkes whether the cars speed is correct
#
speed = int(input('Enter car speed in km/h'))
is_correct = 40 <= speed <= 140
print(f'Speed is correct: {is_correct}')