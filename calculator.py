#calculator.py
""" Simple calculator with basic functionality """
from tkinter import *
root = Tk()
root.title("Simple Calculator")


v = StringVar()
entry = Entry(root, textvariable=v, width = 30, borderwidth=5)
entry.grid(row=0, columnspan=4)

operators = ["+", "-", "/", "*"]
ops = []
numbers = []
number = []
num_list = []

def num_input(character):
    number.append(character)
    v.set("".join(num_list) + "".join(number))
    
def math_add():
    num_list.append("".join(number))
    num_list.append("+")
    number.clear()
    v.set("".join(num_list))

def math_subtract():
    num_list.append("".join(number))
    num_list.append("-")
    number.clear()
    v.set("".join(num_list))

def math_multiply():
    num_list.append("".join(number))
    num_list.append("*")
    number.clear()
    v.set("".join(num_list))

def math_divide():
    num_list.append("".join(number))
    num_list.append("/")
    number.clear()
    v.set("".join(num_list))

def clear_all():
    num_list.clear()
    number.clear()
    ops.clear()
    numbers.clear()
    v.set("".join(num_list))

def math_equals():
    num_list.append(number)
    result = 0
    for i in num_list:
        if i not in operators:
            numbers.append(float("".join(i)))
        else:
            ops.append(i)
    result += numbers[0]
    for i in range(1,len(numbers)):
        if ops[i-1] == "+":
            result += numbers[i]
        elif ops[i-1] == "-":
            result -= numbers[i]
        elif ops[i-1] == "*":
            result *= numbers[i]
        elif ops[i-1] == "/":
            result /= numbers[i]
    if str(result).endswith(".0"):
        result = int(result)
    v.set(result)

# number buttons
one = Button(root, text="1", command=lambda: num_input("1"), height=3, width=4)
one.grid(row=3, column=0)
two = Button(root, text="2", command=lambda: num_input("2"), height=3, width=4)
two.grid(row=3, column=1)
three = Button(root, text="3", command=lambda: num_input("3"),height=3, width=4)
three.grid(row=3, column=2)
four = Button(root, text="4", command=lambda: num_input("4"),height=3, width=4)
four.grid(row=2, column=0)
five = Button(root, text="5", command=lambda: num_input("5"),height=3, width=4)
five.grid(row=2, column=1)
six = Button(root, text="6", command=lambda: num_input("6"),height=3, width=4)
six.grid(row=2, column=2)
seven = Button(root, text="7", command=lambda: num_input("7"),height=3, width=4)
seven.grid(row=1, column=0)
eight = Button(root, text="8", command=lambda: num_input("8"),height=3, width=4)
eight.grid(row=1, column=1)
nine = Button(root, text="9", command=lambda: num_input("9"),height=3, width=4)
nine.grid(row=1, column=2)

# Function buttons
add = Button(root, text="+", command=lambda: math_add(), height=3, width=4)
add.grid(row=1, column=3)
subtract = Button(root, text="-", command=lambda: math_subtract(), height=3, width=4)
subtract.grid(row=2, column=3)
multiply = Button(root, text="*", command=lambda: math_multiply(), height=3, width=4)
multiply.grid(row=3, column=3)
divide = Button(root, text="/", command=lambda: math_divide(), height=3, width=4)
divide.grid(row=4, column=3)
equals = Button(root, text="=", command=lambda: math_equals(), height=3, width=4)
equals.grid(row=4, column=2)
clear = Button(root, text="C", command=lambda: clear_all(), height=3, width=4)
clear.grid(row=4, column=1)
dot = Button(root, text=".", command=lambda: num_input("."), height=3, width=4)
dot.grid(row=4, column=0)


root.mainloop()