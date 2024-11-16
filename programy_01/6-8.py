###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter second letter: ')

number_of_letters = abs(ord(first) - ord(last)) - 1

if number_of_letters == -1:
    print(f'Between {first} and {last} is 0 letters')
else:
    print(f'Between {first} and {last} is {number_of_letters} letters')
