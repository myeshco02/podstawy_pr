def flatten2D(x):
    # Initialize an empty list to store the flattened array
    flat = []
    
    # Iterate through each row of the 2D matrix
    for row in x:
        # Append each element of the row to the flattened list
        flat.extend(row)
    
    return flat

# Example 2D arrays
matrix1 = [
    [2, 3],
    [1, 5]
]

matrix2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Convert the 2D arrays to 1D and print the result
print("Flat array for matrix1:", flatten2D(matrix1))
print("Flat array for matrix2:", flatten2D(matrix2))
print("Flat array for matrix3:", flatten2D(matrix3))
