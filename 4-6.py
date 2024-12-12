###
# Function that returns the full name of a day of the week
# based on its number
#
def day_of_the_week(day_number):
    result = ''
    if day_number == 1:
        result = 'Poniedziałek'
    elif day_number == 2:
        result = 'Wtorek'
    elif day_number == 3:
        result = 'Środa'
    elif day_number == 4:
        result = 'Czwartek'
    elif day_number == 5:
        result = 'Piątek'
    elif day_number == 6:
        result ='Sobota'
    elif day_number == 7:
        result = 'Niedziela'
    else:
        result = 'Nie istnieje'
    return result

def main():
    print("Program podaje nazwę dnia tygodnia na podstawie jego numeru")
    day_number = int(input("Podaj numer dnia tygodnia: "))
    day_name = day_of_the_week(day_number)
    print(f"Dzień tygodnia o numerze {day_number}:", day_name)

main()
