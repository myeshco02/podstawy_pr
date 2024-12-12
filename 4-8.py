def time_string(hours, minutes, time_format):
    """
    Funkcja zwracająca czas w podanym formacie (24-godzinnym lub 12-godzinnym).
    
    Args:
    hours (int): Liczba godzin (0–23)
    minutes (int): Liczba minut (0–59)
    time_format (str): Format czasu ('24' dla 24-godzinnego, '12' dla 12-godzinnego)
    
    Returns:
    str: Czas w odpowiednim formacie
    """
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        period = "am" if hours < 12 else "pm"
        adjusted_hours = hours % 12
        if adjusted_hours == 0:  # Godzina 0 i 12 to 12 w formacie 12-godzinnym
            adjusted_hours = 12
        return f"{adjusted_hours}:{minutes:02}{period}"
    else:
        raise ValueError("Invalid time format. Use '24' or '12'.")

# Program testujący funkcję
def main():
    test_cases = [
        (15, 38, '24', '15:38'),
        (8, 3, '24', '08:03'),
        (0, 5, '24', '00:05'),
        (11, 15, '12', '11:15am'),
        (0, 7, '12', '12:07am'),
        (7, 30, '12', '7:30am'),
        (12, 46, '12', '12:46pm'),
        (13, 10, '12', '1:10pm'),
        (19, 2, '12', '7:02pm'),
    ]
    
    print("Sprawdzanie funkcji time_string:")
    for hours, minutes, time_format, expected in test_cases:
        result = time_string(hours, minutes, time_format)
        print(f"time_string({hours}, {minutes}, '{time_format}') -> {result} (Oczekiwane: {expected})")
        assert result == expected, f"Błąd: otrzymano {result}, oczekiwano {expected}"
    print("Wszystkie testy zakończone sukcesem!")

# Wywołanie programu testującego
main()
