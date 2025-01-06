import json

# Open the JSON file in read mode with utf-8 encoding
with open('dogs.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    data = json.load(file)

# Print the information about dogs younger than 5 years
for dog in data:
    if dog['age'] < 5:
        for key, value in dog.items():
            print(f"{key}: {value}")
        print()
