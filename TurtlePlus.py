import turtle as tl

# add more shapes
def square(float):
    for i in range(4):
        tl.forward(float)
        tl.left(90)
        
def triangle(float):
    for i in range(3):
        tl.forward(float)
        tl.left(120)
        
def pentagon(float):
    for i in range(5):
        tl.forward(float)
        tl.left(72)
        
def hexagon(float):
    for i in range(6):
        tl.forward(float)
        tl.left(60)

def octagon(float):
    for i in range(8):
        tl.forward(float)
        tl.left(45)

def zigzag(float):
    for i in range(float):
        tl.left(50)
        tl.forward(35)
        tl.right(50)
        tl.forward(35)