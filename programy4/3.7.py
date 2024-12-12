array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest=""

for i in array:
    if len(i) > len(longest):
        longest = i
    
print(f"All names: {array} ")
print(f"Longest name: {longest} ")
