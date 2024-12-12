# main.py

import keyboard  # Importowanie własnego modułu

# Odczyt danych pracownika z klawiatury
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')

# Wyświetlenie danych pracownika
print('DATA RECORD')
print('===========')
print(f'Name: {first_name} {last_name}')
print(f'Age: {age}')
if not is_salary_hidden:
    print(f'Salary: {salary}')
else:
    print('Salary: [Hidden]')
