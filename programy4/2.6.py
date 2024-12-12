array = []
for i in range(3):
    row = [] #creates subarray (we can call it "inner array")
    for j in range (3):
        if i == j: #for every iteration of this loop if compares i and j
            row.append(1) #if they are the same adds 1 as an alement of inner array
        else:
            row.append(0) #else it adds 0 as the element of inner array
    array.append(row) #after inner for is done this line adds whole new inner array into the main "2D" array, our designed target
    
for row in array: #this loop prints every row (inner array) in new line so it looks like a matrix
    print(row)

for x in range(20):         #simple line created by a lazy guy ;)
    print("=", end="")
print ("")

#in later examples I'll use a simpler one line version of this code :)
arraySimple = [[1 if i == j else 0 for j in range(3)] for i in range(3)]

for row in arraySimple:
    print(row)
