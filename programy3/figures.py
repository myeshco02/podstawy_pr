def draw_square(t, length):
    # Rysuje kwadrat na podstawie boku
    for _ in range(4):
        t.forward(length)
        t.right(90)

def draw_triangle(t, length):
    # Rysuje trójkąt
    for x in range(3):
        t.forward(length)
        t.left(120)

def draw_rectangle(t, length_a, length_b):
    # Rysuje prostokąt
    for x in range(2):
        t.forward(length_a)
        t.right(90)
        t.forward(length_b)
        t.right(90)
