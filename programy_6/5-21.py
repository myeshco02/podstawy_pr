import json

# Słownik opisujący film "Zwierzogród"
favorite_movie = {
    "title": "Zootopia",
    "director": "Byron Howard, Rich Moore",
    "release_year": 2016,
    "genre": "Animation, Adventure, Comedy",
    "main_characters": ["Judy Hopps", "Nick Wilde"],
    "studio": "Walt Disney Animation Studios",
    "rating": 8.0,
    "awards": ["Academy Award for Best Animated Feature"]
}

# Określenie nazwy pliku
file_name = "favorite.json"

# Zapisanie słownika do pliku JSON
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(favorite_movie, file, indent=4)

print("Dane zostały zapisane do", file_name)
