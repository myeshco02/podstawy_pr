# Dane o cenniku przed rabatem
price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

# 1. Wypisanie listy produktów i ich cen przed rabatem
print("Lista produktów i ceny przed rabatem:")
for product, price in price_list.items():
    print(f'{product}: {price:.2f}')

# 2. Obliczenie całkowitej wartości produktów przed rabatem
total_before_discount = sum(price_list.values())
print(f'\nCałkowita wartość produktów przed rabatem: {total_before_discount:.2f}')

# 3. Modyfikowanie cennika o rabat 10% i zaokrąglanie cen do dwóch miejsc po przecinku
discounted_price_list = {product: round(price * 0.9, 2) for product, price in price_list.items()}

# 4. Wypisanie listy produktów i ich cen po rabacie
print("\nLista produktów i ceny po rabacie:")
for product, discounted_price in discounted_price_list.items():
    print(f'{product}: {discounted_price:.2f}')

# 5. Obliczenie całkowitej wartości produktów po rabacie
total_after_discount = sum(discounted_price_list.values())
print(f'\nCałkowita wartość produktów po rabacie: {total_after_discount:.2f}')
