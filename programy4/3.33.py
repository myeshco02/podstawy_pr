arr = [
    [1, 2, 3, 4, 5], #row[0]
    [6, 7, 8, 9, 10], #row[1]
    [11, 12, 13, 14, 15] #row[2]
]

print("Entry array: ")
for row in arr:
    print(row)

for row in arr:   
    row[0], row[-1] = row[-1],row[0] #swapping first element in every row (index 0) with last element (index -1)

print("")
print("Array after swapping rows: ")
for row in arr:
    print(row)
