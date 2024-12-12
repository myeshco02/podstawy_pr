#inputs size of array
x=int(input("Enter x size of array: "))
y=int(input("Enter y size of array: "))

#ensures that size is above 0
if x<=0 or y<=0:
    print("SIZE NEEDS TO BE BIGGER THAN 0 !!!")
    exit()
else:
    arr=[[0 for i in range(x)] for j in range(y)] #first 0 for i in range(x) generates number of 0 in row based on x(number of columns), and outside loop generates row y times (number of rows)
    for row in arr:
        print(row)
