week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#user inputs a number between 1 - 7, checking if it is correct
x = int(input('Input number between 1-7: '))
if 1 <= x <= 7:
    print('correct X :3')
    print(week[x-1])
else:
    print('Enter correct X !!!')

#printing day 1, 4, 7 using defined function
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]
    
print(weekday(1))
print(weekday(4))
print(weekday(7))
