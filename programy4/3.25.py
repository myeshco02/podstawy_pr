#link for online compiler https://www.tutorialspoint.com/execute_matplotlib_online.php

import matplotlib.pyplot as plt

x = []
y = []

# array used for drawing function y(x)
for n in range(-100, 101):
    x.append(n)

# loop generating y values
for n in x:
    y.append(n**2 - 3)

# .plot draws graph
plt.plot(x, y, label="f(x) = x^2 - 3")

#Labels x and y axis 
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Adds title on top of graph
plt.title("Graph of f(x) = x^2 - 3")

# Adds a legend
plt.legend()

# Adds gridlines
plt.grid()

# Shows the plot
plt.show()
