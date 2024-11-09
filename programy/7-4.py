circumference = int(input('Enter tree circumference in cm: '))
diameter_ok = circumference / 3.14 >= 50
print(f'Tree can be cut down: {diameter_ok}')