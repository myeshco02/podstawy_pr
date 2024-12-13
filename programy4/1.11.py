# The weather station report
#
temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# number of mesaurements
mesaurements = len(temperatures)

# calculates average temperature
temp_total = 0
for temp in temperatures:
   temp_total += temp
avg_temp = temp_total / mesaurements

# calculates min and max temperatures
min_temp = min(temperatures)
max_temp = max(temperatures)

# calculates number of days with negative temp
negative_temp = 0
i = 0
while i < len(temperatures):
   if temperatures[i] < 0:
      negative_temp +=1
   i += 1

# prints out month report
print('Month: March')
print(f"Number of mesaurements: {mesaurements} ")
print(f"Average temeratures: {avg_temp} ")
print(f"Minimum temp: {min_temp} ")
print(f"Maximum temp: {max_temp} ")
print(f"Number of days with negative temp: {negative_temp} ")

