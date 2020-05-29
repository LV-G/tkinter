# grid.py
""" Simple script to explore use of buttons in tkinter gui interface """
from tkinter import *

root = Tk()

def my_click():
    my_label=Label(root, text="You clicked the button")
    my_label.grid(row=0, column=1)

my_button1 = Button(root, text="This button is Disabled", state=DISABLED)
my_button2 = Button(root, text="This button is Enabled", padx=20, pady=25, command=my_click, bg="#000000", fg="#ffffff")
my_button1.grid(row=0, column=0)
my_button2.grid(row=0, column=1)

root.mainloop()
