#The speed of vehicles on highways in Poland is
#at least 40 km/h and not more than 140 km/h
#write a program that prints a message
#when the specified car speed, read from the keyboard, has been exceeded.

car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
else:
    print('Valid car speed')
