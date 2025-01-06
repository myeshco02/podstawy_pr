products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

print("Lista produktów i ilość: ")
for key,value in products.items():
    print(f"{key}:{value}")

total_products = sum(products.values())
print(f"Całkowita ilość produktów: {total_products}")
