'''
Created on 17 Dec. 2018

@author: Jihan
'''

if __name__ == '__main__':
    pass

import turtle


def draw_multicolor_square(animal, size):  # """Make animal draw a multi-color square of given size."""
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)

        
window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")
tess = turtle.Turtle()  # Create tess and set some attributes
tess.pensize(3)

size = 20  # Size of the smallest square
for _ in range(45):
    draw_multicolor_square(tess, size)
    size += 10  # Increase the size for next time
    tess.forward(10)  # Move tess along a little
    tess.right(8)  # and give her some turn

window.mainloop()
