# grid.py
""" Simple script to explore use of buttons in tkinter gui interface """
from tkinter import *

root = Tk() # Create root widget

entry = Entry(root, width=50, borderwidth=10, bg="#000000", fg="#ffffff") # create basic entry box in root
entry.grid(row=1, column=0)
entry.insert(0, "Enter your name")
# Create function for label creation
def my_click():
    message = entry.get()
    my_label=Label(root, text="Thank you " + message)
    my_label.grid(row=2, column=0)

# Create button and define action on click
my_button = Button(root, text="Confirm", padx=20, pady=25, command=my_click, bg="#000000", fg="#ffffff")
my_button.grid(row=0, column=0)

# Run root widget
root.mainloop()
