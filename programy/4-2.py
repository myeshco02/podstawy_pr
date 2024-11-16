###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members

print(f'Total family income is {total_income: ,.2f}PLN, and income per person is {income_per_person: ,.2f}PLN.' .replace(',', ' ')
)

#liczby w walucie mogą być z dokładnością maksymalnie do 2 miejsc po przecinku (grosze, centy) 
#stąd formatowanie do 2 miejsc po przecinku

#użyto separatora jednak taki separator nie powinien być używany w UE
#stąd zamiana separatora na spację
