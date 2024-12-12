def f(name):
    # Podzielamy tekst na słowa, bierzemy pierwszą literę każdego słowa, konwertujemy na wielką literę i łączymy
    return ''.join(word[0].upper() for word in name.split())

print(f("Internet of Things"))  # wynik: "IoT"
print(f("For Your Information")) # wynik: "FYI"
print(f("Python"))              # wynik: "P"
