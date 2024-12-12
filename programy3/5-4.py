import turtle
from figures import draw_square

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightblue")

# Draw a square using the imported function
draw_square(100)

# Finish
window.mainloop()
