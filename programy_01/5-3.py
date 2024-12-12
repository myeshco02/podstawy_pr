###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_string = input('a=')
b_string = input('b=')
c_string = input ('c=')

a = float(a_string)
b = float(b_string)
c= float(c_string)


if a>0 and b>0 and c>0:
    volume = a * b * c
    surface = 2 * a * b + 2 * b * c + 2 * a * c

    print(f'Volume of the cuboid is: {volume} ')
    print(f'Surface of the cuboid is: {surface} ')
else:
    print("Wprowadzono niewłaściwe wymiary.")

#dodano if - sprawdza czy wartości mają sens