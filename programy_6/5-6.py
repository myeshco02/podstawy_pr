# Dwa słowniki z danymi osobowymi
basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# Łączenie dwóch słowników w jeden
person = {**basic_data, **advanced_data}

# Wydrukowanie zawartości słownika person
print("Combined person dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
