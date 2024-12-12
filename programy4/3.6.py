array = [15, 8, 31, 47, 2, 19]

sumArray = 0
i=0
while i < len(array):
    value = array[i]
    sumArray += value
    i+=1
mean = sumArray / len(array)

print(mean)
