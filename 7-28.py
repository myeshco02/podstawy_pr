def f(dice):
    if not dice:  # Obsługa pustej sekwencji
        return 0
    
    max_streak = 1  # Maksymalna liczba powtórzeń
    current_streak = 1  # Aktualna liczba powtórzeń
    
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:  # Jeśli bieżąca cyfra jest taka sama jak poprzednia
            current_streak += 1
        else:  # Jeśli ciąg się kończy
            max_streak = max(max_streak, current_streak)
            current_streak = 1
    
    # Ostatni ciąg może być najdłuższy
    max_streak = max(max_streak, current_streak)
    
    return max_streak



print(f("5233165554211"))  # wynik: 3
# Najdłuższy ciąg: '555' (długość 3)

print(f("2133"))  # wynik: 2
# Najdłuższy ciąg: '33' (długość 2)

print(f(""))  # wynik: 0
# Pusta sekwencja zwraca 0

print(f("11111"))  # wynik: 5
# Cała sekwencja to jeden ciąg (długość 5)
