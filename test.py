import turtle as tl
import TurtlePlus as tlp

# setup window
tl.setup(800,600)

# setup pen
tl.pencolor("black")
tl.pensize(2.5)

# draw something
tlp.square(-100)
tlp.zigzag(5)
tlp.octagon(50)

# setup loop
tl.mainloop()