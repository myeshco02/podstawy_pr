import queue

# creates a stack
stack = queue.LifoQueue()

# adds elements to the top of the stack
stack.put(2)  # Push 2 onto the stack
stack.put(3)  # Push 3 onto the stack
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Zsumowanie dwóch ostatnich liczb na stosie
last_number = stack.get()  # Usuwamy i zapisujemy ostatni element (8)
second_last_number = stack.get()  # Usuwamy i zapisujemy przedostatni element (9)
sum_last_two = last_number + second_last_number
print("Suma dwóch ostatnich liczb:", sum_last_two)

# Obliczenie sumy pozostałych elementów stosu
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()  # Dodajemy każdy element do sumy
print("Suma pozostałych elementów:", remaining_sum)
