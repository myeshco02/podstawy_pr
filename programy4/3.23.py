def text(x):
    return " ".join(x)

def wordCount(x):
    count=0
    for i in x:
        count+=1
    return count

def longToShort(x):
    return ", ".join(sorted(x, key=len))
    
def alphSort(x):
    return ", ".join(sorted(x))
    

arr=["An", "apple", "a", "day", "keeps", "the", "doctor", "away"]
print(f"Text: {text(arr)} ")
print(f"Number of words: {wordCount(arr)} ")
print(f"Words by lengh: {longToShort(arr)} ")
print(f"Words aplhabetically: {alphSort(arr)} ")
