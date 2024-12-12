#Most female names in Polish end with the letter "a".
#Write a program that prints the name entered
#from the keyboard, provided it is a female name.

name = input('What is your name?: ')

#Checking if the last character to lower case is an "a"
if name[-1].lower() == 'a':
    print(f'{name} is polish female name')
else:
    print(f'{name} is not a polish female name')
