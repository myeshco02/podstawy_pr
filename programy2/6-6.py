#The parking meter calculates the parking fee based on the number of
#hours the car was parked according to the following rules:
#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN


parking_fee = 0
parking_hours = int(input("How many hours have you been parked?: "))

if parking_hours >= 1 and parking_hours <= 2:
    print("You have to pay 5 PLN")
elif parking_hours <= 6:
    print("You have to pay 15 PLN")
elif parking_hours > 6:
    print("You have to pay 20 PLN")
else:
    print("You are free of charge")
