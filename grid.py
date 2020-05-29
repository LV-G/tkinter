# grid.py
""" Simple script to explore use of grid positioning in tkinter gui interface """
from tkinter import *

root = Tk()

# Creating a label with tkinter
my_label1 = Label(root, text="This is the first label")
my_label2 = Label(root, text="This is the second label")
my_label3 = Label(root, text="This is the third label")

# Shoving it onto the screen

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=3)
my_label3.grid(row=0, column=2)

root.mainloop()
