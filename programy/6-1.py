###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Jan'   # replace Anna with your name
#imie i nazwisko przykładowe
surname = 'Kowalski' # replace May with your surname
characters_in_name = len(name)
characters_in_surname = len(surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_name + characters_in_surname + 1 } characters') # with a space between name and surname
#+1 jeśli liczymy ze spacją, jeśli bez spacji to bez '+1'