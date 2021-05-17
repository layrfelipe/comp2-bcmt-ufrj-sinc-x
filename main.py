from tkinter import *
from DigitalClock import *
from ResizableCanvas import ResizingCanvas
import os
from math import pi, sin
import sys

# Constants used to create Canvas widget
VX = 256
VY = 128

# Toplevel widget configuration
root = Tk()
root.geometry("524x256")

# Rightside frame containing a digital clock, an image and a button
right = Frame(root, bg="#cccccc", borderwidth=2, relief="raised")
right.pack(fill = "y", side="right")

# On the left, a big container for displaying graphics
canvasFrame = Frame(root, bg="#cccccc")
canvasFrame.pack(fill="both", expand=1)

clockLabel = Label(right, bg="gray", font=('times 28', 16, 'bold'))
clockLabel.pack(side="top")

# Separated thread just for the clock
d = digitalClock(clock=clockLabel)
t = makeThread(d.tick)
t.start()

# Ends thread
def handleStopThreadCallback():
    return sys.exit()

# Image settings
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'flu.gif')
flu = PhotoImage(file=image_path)
label = Label(right,image=flu, bg="#cccccc")
label.pack(side='top', pady=50, expand=1, fill="both")

b1 = Button(right, text="Finalizar", command=handleStopThreadCallback)
b1.pack(side="bottom", fill="x")

# Class built and given by the professor for not distort graphics in Canvas widget
myCanvas = ResizingCanvas(canvasFrame, width=2*VX, height=2*VY, bg="#cccccc", highlightthickness=0)
myCanvas.pack(expand=1, fill="both")

# Cartesian coordinates array
pts = []

# Cartesian axes
myCanvas.create_line(VX, 0, VX, 2*VY, fill="black")
myCanvas.create_line(0, VY, 2*VX, VY, fill="black")

for xc in range (-VX, VX):
    if xc == 0:
        x_coord = 0
        y_coord = 1
    else:
        x_coord = (((15*pi*xc) / VX)) # Mapping for 15 ridges each side (professor's request)
        y_coord = int((((-sin(x_coord)) / x_coord) * VY) + VY)
    pts += [[xc + VX, y_coord]]

myCanvas.create_line(*pts, fill="red", width=3)

root.mainloop()