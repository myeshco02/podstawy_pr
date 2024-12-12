arraySimple1 = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
arraySimple2 = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
arraySimple3 = [[1 if i == j else 0 for j in range(8)] for i in range(8)]

for row in arraySimple1:
    print(row)
print("")

for row in arraySimple2:
    print(row)
print("")

for row in arraySimple3:
    print(row)
print("")
