import turtle as tl
import turtleplus as tlp
import colorsys as csys

# setup variables
h = 0

# setup window
tl.setup(1050,800)
tl.bgcolor("black")

# setup pen
tl.pencolor()
tl.pensize(2.5)
tl.goto(-475,-350)

# draw something
for i in range(15):
    c = csys.hsv_to_rgb(h, 1, 1)
    h += 0.075
    
    tl.color(c)
    tlp.square(10+i)
    tl.forward(10+i)
    tlp.zigzag(3)
    
# setup loop
tl.mainloop()