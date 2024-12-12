arr = [1, 2, 3, 2, 4, 5, 1, 6]

unique = [] #array of unique values
seen = set() #set of already "seen" elements

for i in arr:
    if i not in seen: #if element is not in set called seen we go through
        unique.append(i)  #add element to array unique
        seen.add(i)  #add element into set seen to count it as already used

print("Starting array: ", arr)
print("Unique elements:", unique)
