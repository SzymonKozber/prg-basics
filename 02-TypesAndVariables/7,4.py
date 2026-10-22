###
# A program that checks whether the tree can be cut down based on its diameter.
# The tree can be cut down if its diameter is greater than 50 cm.
circumference = float(input('Enter tree circumference in cm: '))
diameter = circumference / 3.14
can_be_cut_down = diameter > 50
print(f'Tree can be cut down: {can_be_cut_down}')