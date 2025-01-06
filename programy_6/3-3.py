import queue

def brackets_ok(expression):
    # Tworzymy stos
    stack = queue.LifoQueue()

    # Mapa nawiasów zamykających do odpowiadających nawiasów otwierających
    matching_brackets = {')': '(', '}': '{', ']': '['}

    # Przechodzimy przez każdy znak wyrażenia
    for char in expression:
        if char in "({[":  # Jeśli to nawias otwierający
            stack.put(char)
        elif char in ")}]":  # Jeśli to nawias zamykający
            if stack.empty():  # Jeśli stos jest pusty, ale napotkaliśmy nawias zamykający
                return False
            top = stack.get()  # Pobieramy element ze stosu
            if top != matching_brackets[char]:  # Sprawdzamy, czy pasuje do odpowiadającego nawiasu
                return False

    # Jeśli stos jest pusty, to znaczy, że wszystkie nawiasy zostały poprawnie zamknięte
    return stack.empty()

# Przykładowe wyrażenia
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # nawiasy poprawne
expression2 = "[(2+3]/4)"                 # nawiasy niepoprawne
expression3 = "(2-3*4+(5/6)"              # nawiasy niepoprawne

# Sprawdzamy poprawność wyrażeń
if brackets_ok(expression1):
    print("Expression 1: Brackets are correct.")
else:
    print("Expression 1: Brackets are incorrect.")

if brackets_ok(expression2):
    print("Expression 2: Brackets are correct.")
else:
    print("Expression 2: Brackets are incorrect.")

if brackets_ok(expression3):
    print("Expression 3: Brackets are correct.")
else:
    print("Expression 3: Brackets are incorrect.")
