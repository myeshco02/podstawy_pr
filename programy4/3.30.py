x,y = 5,5

#prints array in size 5x5 full of 0
arr = [[0 for i in range(x)] for i in range(y)]
#print(arr)

#every index in array is replaced by multiplication 
for i in range(x):
    for j in range(y):
        arr[i][j] = (i+1) * (j+1) 

for row in arr:
    print(row)
