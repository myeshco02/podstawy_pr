# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
# Calculates expenses
# Use loop statements

#Food
sumFood = sum(row[0] for row in monthly_expenses)

#Transport
sumTrans = sum(row[1] for row in monthly_expenses)

#Utilities
sumUtil = sum(row[2] for row in monthly_expenses)

#Week 1
w1 = sum(monthly_expenses[0])

#Week 2
w2 = sum(monthly_expenses[1])

#Week 3
w3 = sum(monthly_expenses[2])

#Week 4
w4 = sum(monthly_expenses[3])

#monthlyexpenses
monthSum=0
for row in monthly_expenses:
    for price in row:
        monthSum+=price
    print()

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', sumFood)
print('Transport:',sumTrans)
print('Utilities:',sumUtil)
print('Week 1:',w1)
print('Week 2:',w2)
print('Week 3:',w3)
print('Week 4:',w4)
print('---------------')
print('TOTAL:', monthSum)
