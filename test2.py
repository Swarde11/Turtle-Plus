import turtle as tl
import turtleplus as tlp
import colorsys as csys

h = 0

# setup window
tl.setup(1050,800)
tl.bgcolor("black")
tl.goto(-400,-350)

# draw something
for i in range(100):
    c = csys.hsv_to_rgb(h, 1, 1)
    h += 0.025
    
    tl.color(c)
    tlp.hexagon(25 +--+ i * 2)
    tl.speed(10 * i)

# setup loop
tl.mainloop()