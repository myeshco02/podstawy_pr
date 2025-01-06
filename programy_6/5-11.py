import json
import os

# Ścieżka do pliku z wynikami głosowania
FILE_PATH = 'voting.json'

def load_voting_data():
    """Funkcja wczytująca dane z pliku JSON."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}  # Zwróć pusty słownik, jeśli plik jest uszkodzony
    return {}

def save_voting_data(data):
    """Funkcja zapisująca dane do pliku JSON."""
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    """Główna funkcja programu."""
    # Wczytanie aktualnych wyników głosowania
    voting_data = load_voting_data()

    # Pobranie imienia osoby do głosowania
    person_name = input('Name of the person you are voting for: ').strip()

    if not person_name:
        print("Invalid input. Name cannot be empty.")
        return

    # Aktualizacja liczby głosów
    if person_name in voting_data:
        voting_data[person_name] += 1
    else:
        voting_data[person_name] = 1

    # Zapisanie zaktualizowanych wyników głosowania
    save_voting_data(voting_data)

    print(f"Vote registered for {person_name}! Current votes:")
    for name, votes in voting_data.items():
        print(f"{name}: {votes}")

if __name__ == '__main__':
    main()
