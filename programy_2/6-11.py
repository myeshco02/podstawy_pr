#A computer program analyses the price of a product in an online store.
#If the product price decreases by at least 10%
#the program prints a purchase recommendation

Current_product_price = 170.00
Previous_product_price = 200.00

obnizka = (1 - (Current_product_price / Previous_product_price)) * 100
obnizka = int(obnizka)

if obnizka > 10:
    print('Buy the product!!')
    print(f'Product price reduced by {obnizka}%')
elif obnizka <= 0:
    print('Do not buy the product!!')
    print('Product is not reduced')
else:
    print('Do not buy the product!!')
    print(f'Product price reduced by {obnizka}%')
