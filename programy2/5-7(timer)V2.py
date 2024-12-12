###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

# definiujemy dziennik
words = {5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}

while countdown > 0:
    if countdown <= 5:
        print(words[countdown])
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")
