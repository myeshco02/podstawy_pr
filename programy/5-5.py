while True:


    cena_in = input('Podaj cenę: ')
    try:
        cena = float(cena_in)
    except ValueError:
        print("Upewnij się, że wprowadzasz liczbę.")
        continue
    if cena != round(cena, 2):
        print('Wprowadź max 2 miejsca po przecinku')
        continue


    while True:
        sale_proc_in = input('Podaj' ' %'  ' obniżkę: ')
        try:
            sale_proc = int(sale_proc_in)
        except ValueError:
            print("Upewnij się, że wprowadzasz liczbę.")
            continue
        if (sale_proc < 0 or sale_proc > 100):
            print('Wprowadzono wadliwą obniżkę')
            continue

        sale = cena * sale_proc /100
        cena_po_sale = cena - sale

        print(f'Cena po obniżce wynosi: {cena_po_sale: ,.2f} PLN')
        print(f'Rabat wyniósł: {sale: ,.2f} PLN')
        break
    break