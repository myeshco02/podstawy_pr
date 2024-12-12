arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

minArr = float('inf') #number close to infinity is used to be certain than first number we check is lower 
maxArr=float('-inf') #number close to neg infinity is used to be certain that first number is higher 
minPos=(0, 0) #paceholders for position 
maxPos=(0,0)
for i in range(len(arr)):
    for j in range(len(arr[i])): #we loop through every item in array
        value=arr[i][j] #value of array element we want to check right now
        if value < minArr: #value of element is lower than the actual lowest number
            minArr=value
            minPos=(i,j) # we asign its value to minArr and its position to minPos
        if value > maxArr:
            maxArr = value
            maxPos=(i,j)   #same logic is aplied in this loop, checking if number is highest and saving its value and position
            
print(f"Smallest number is: {minArr}, on position {minPos} ")
print(f"Biggest number is: {maxArr}, on position {maxPos} ")
