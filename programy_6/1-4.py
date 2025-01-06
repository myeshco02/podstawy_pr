"""
person = {
   "name": "Marek", ---> string
   "surname": "Banach", ---> string
   "age": 25, ---> integer
   "hobby": ["swimming","excursions"], ---> list
   "married": True, ---> boolean
   "phone":{"landline":"123444321","mobile":"777888999"} ---> dictionary
}
"""

person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

# Wyświetlanie imienia
print(person["name"])

#Wyświetlanie hobby
print(person["hobby"])

#Wyświetlanie całej zawartości słownika
for key,value in person.items():
    print(f"{key}: {value}")

#Zmiana nazwiska
person["surname"] = "Nowak"

# Zmiana statusu małżeńskiego
person["married"] = not person["married"]

# Dodanie płci
person["gender"] = "mężczyzna"

# Dodanie nowego hobby
person["hobby"].append("rower")

# Dodanie telefonu służbowego
person["phone"]["work"] = "313131444"

# Wyświetlanie całej zawartości słownika po modyfikacjach
for key, value in person.items():
    print(f"{key}: {value}")