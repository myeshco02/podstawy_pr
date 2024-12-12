# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle
from figures import draw_square, draw_triangle, draw_rectangle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tworzy żółwia
pen = turtle.Turtle()
pen.speed(5)   

## 
# Pierwszy kwadrat
pen.penup()  #Podnosi długopis bez rysowania
pen.goto(-200, 200)  #Przesuwa długopis bez rysowania
pen.pendown()  #Odkłada długhopis
draw_square(pen, 100)  

#Drugi kwadrat w innej lokalizacji
pen.penup()
pen.goto(100, 200)
pen.pendown()
draw_square(pen, 100)

pen.penup()
pen.goto(-200, -100)
pen.pendown()
draw_triangle(pen, 100)

pen.penup()
pen.goto(100, -100)
pen.pendown()
draw_triangle(pen, 100)

pen.penup()
pen.goto(-200, -200)
pen.pendown()
draw_rectangle(pen, 150, 100)

pen.penup()
pen.goto(100, -200)
pen.pendown()
draw_rectangle(pen, 150, 100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()