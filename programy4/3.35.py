def transMatrix(x):
    # Create an empty list to store the transposed matrix
    transposed = []
    
    # loops through every column (x[0] indicates first row of column and loop goes through every element in row)
    for col in range(len(x[0])):
        # Create new row for every loop
        newRow = []
        
        #Loop through every row in default array
        for row in x:
            # Add current element (from each row, same column because row[col]) to the new row
            newRow.append(row[col])
        #The loop above "converts" every element in particular column to row 
        # Append a row created by the loop to our transposed array
        transposed.append(newRow)
    
    return transposed
    
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7, 8]
]
transposedMatrix1 = transMatrix(matrix1)
transposedMatrix2 = transMatrix(matrix2)
transposedMatrix3 = transMatrix(matrix3)


print("Original array 1: ")
for row in matrix1:
    print(row)

print("Transposed matrix 1: ")
for row in transposedMatrix1:
    print(row)

print("Original array 2: ")
for row in matrix2:
    print(row)

print("Transposed matrix 2: ")
for row in transposedMatrix2:
    print(row)

print("Original array 3: ")
for row in matrix3:
    print(row)

print("Transposed matrix 3: ")
for row in transposedMatrix3:
    print(row)
