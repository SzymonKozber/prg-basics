###
# A simple countdown timer that prints numbers in words for 1 to 5 and numbers for 6 and above.
#

import time

countdown = int(input("Enter the number of seconds to count down: "))

# Dictionary mapping numbers 1 through 5 to their word equivalents
word_map = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

while countdown > 0:
    # Print the word if countdown is between 1 and 5, otherwise print the number
    print(word_map.get(countdown, countdown))
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")