#Write a program that allows you to convert time
#in 24-hour format to 12-hour format.
#The time in 24-hour format (hh:mm) is read from the keyboard.

time_24h = input('Enter time in 24-hour format(XX:XX) ')

hours = int(time_24h[:2]) #takes 2 last digit from hour (XX  : X X)
minutes = int(time_24h[3:]) # takes 3 first digits ( X X:  XX)

# if its pm or am

if hours >= 12:
    this_stuff_behind_hour = 'pm'
else:
    this_stuff_behind_hour = 'am'

if hours > 12:
    hours -= 12
elif hours == 0:
    hours = 12 #midnight

print(f'Time in 12-hour format: {hours}:{minutes:02d}{this_stuff_behind_hour}')
#:02d robi pelne minuty typu xx:02 a nie xx:2
