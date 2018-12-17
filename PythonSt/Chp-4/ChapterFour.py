'''
Created on 14 Dec. 2018

@author: E491529
'''


if __name__ == '__main__':
    pass



import turtle



window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")
window.title("Tess & Alex")
alex = turtle.Turtle()
alex.color("red")
alex.pensize(15)

for _ in range(4):
    alex.forward(250)
    alex.left(90)
    
    
for colour in ["yellow", "red", "purple", "blue"]:
    alex.color(colour)
    alex.forward(50)
    alex.left(90)
    alex.speed(2)
    alex.shape("turtle")
    
window.mainloop()