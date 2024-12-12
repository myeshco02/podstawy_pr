def occurs(number, array):
    return number in array
    
arr = [15, 38, 7, 23, 14]

num = int(input("Input a number: "))

if occurs(num, arr):
    print(f"Number {num} is in array")
else:
    print(f"Number {num} isnt in array ")
