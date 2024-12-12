categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

#checking max expanses
maxExp = max(expenses)
index = expenses.index(maxExp)

print(f"Most expensive category was {categories[index]}, costing {maxExp}")
