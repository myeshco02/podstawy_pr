###
# Vehicle registration numbers in Krakow start
# with the letters KR or KK. Write a program that checks
# whether the vehicle registration number entered
# from the keyboard means a vehicle from Krakow.
# Print True whether a car is from Krakow or False otherwise.
#
car_number = input('Enter car registration number')
is_krakow = car_number[0:2] in ("KR","KK")
#Uwaga tutaj się podziało inaczej niż ustawodawca przewidział

print(f'Car is from Krakow: {is_krakow}')