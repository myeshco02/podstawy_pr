def f(password):
    # Sprawdzamy, czy długość hasła jest co najmniej 6 znaków
    if len(password) < 6:
        return False
    
    # Sprawdzamy, czy wszystkie znaki w haśle są unikalne
    if len(password) != len(set(password)):
        return False
    
    return True

print(f("ax15"))      # wynik: False (za krótkie hasło)
print(f("book123"))   # wynik: False (powtórzenie "o")
print(f("A2water3"))  # wynik: True (hasło ma co najmniej 6 znaków i brak powtórzeń)
print(f("qwerty"))    # wynik: True (hasło ma co najmniej 6 znaków i brak powtórzeń)
print(f(""))          # wynik: False (puste hasło)
