myTuple = (50,20,30,50,40,50)

def occur(value, data):
    return myTuple.count(value)
    
toCount = 50
count = occur(toCount, myTuple)

print(f"The {toCount} occurs in tuple {count} times. ")
