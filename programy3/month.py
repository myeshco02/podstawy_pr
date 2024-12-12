def month_name():
    month_number = int(input("Podaj numer miesiąca: "))
    if month_number == 1:
        print(f"Miesiąc o numerze {month_number} to: Styczeń")
    elif month_number == 2:
        print(f"Miesiąc o numerze {month_number} to: Luty")
    elif month_number == 3:
        print(f"Miesiąc o numerze {month_number} to: Marzec")
    elif month_number == 4:
        print(f"Miesiąc o numerze {month_number} to: Kwiecień")
    elif month_number == 5:
        print(f"Miesiąc o numerze {month_number} to: Maj")
    elif month_number == 6:
        print(f"Miesiąc o numerze {month_number} to: Czerwiec")
    elif month_number == 7:
        print(f"Miesiąc o numerze {month_number} to: Lipiec")
    elif month_number == 8:
        print(f"Miesiąc o numerze {month_number} to: Sierpień")
    elif month_number == 9:
        print(f"Miesiąc o numerze {month_number} to: Wrzesień")
    elif month_number == 10:
        print(f"Miesiąc o numerze {month_number} to: Październik")
    elif month_number == 11:
        print(f"Miesiąc o numerze {month_number} to: Listopad")
    elif month_number == 12:
        print(f"Miesiąc o numerze {month_number} to: Grudzień")
    else:
        print(f"Miesiąc o numerze {month_number} nie istnieje!")

    if __name__ == "__main__":
        month_name()
