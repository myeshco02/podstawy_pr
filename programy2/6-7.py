#Write a program that asks the user for
#their age and then checks which age group they belong to:
#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older

age = int(input("How old are you?: "))

if age < 0:
    print("You haven't been born yet")
elif age < 13:
    print("Your age group is: Child")
elif age < 20:
    print("Your age group is: Teen")
elif age < 65:
    print("Your age group is: Adult")
else:
    print("Your age group is: Senior")
