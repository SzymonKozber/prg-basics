###
# A program that checks whether the number rolled is special 
#
import random
dice_roll = random.randint(1, 6)
is_special = dice_roll == 1 or dice_roll == 6
print(f'Dice roll: {dice_roll}')
print(f'Is special: {is_special}')