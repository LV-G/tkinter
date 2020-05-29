# hello.py
""" Simple tkinter script to display message onto gui """
from tkinter import *

root = Tk() # Create root widget, must always come first
# Two step process to displaying in tkinter
# Create the object and then display it

my_label = Label(root, text="This is a simple message displayed in a GUI") # Created label object
# Need to put into the root object now, first method is to using pack(unordered)
my_label.pack() # Pack into root widget

# Widget GUI interfaces uses constant looping to refresh the image displayed

root.mainloop() # Loop run until program is ended (press "x" button or ctrl+c)



