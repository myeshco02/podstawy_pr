arr=[2,3,7,5,4]
#prints whole array
print(arr)

#prints nuumber of elements array contains
print(len(arr))

#prints first item in array
print(arr[0])

#prints second item in array
print(arr[1])

#prints last item in array
print(arr[-1])

#prints second to last item in array
secToLast = len(arr) - 2
print(arr[secToLast])

#sum of first and last item
sum = arr[0] + arr[-1]
print(sum)

#item in the middle of array 
midItem = len(arr) // 2 #this works for un-even arrays just fine and for even arrays this method prints the "higher" middle value
print(arr[midItem])

#every array item with single space between
for x in range(len(arr)):
    print(arr[x], end=" ")
