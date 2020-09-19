from tkinter import *
from tkmacosx import Button
import parser
import math

root = Tk()
root.title('Tile rate calculator')

# get user input and place it in the text field
i = 0
global area
global amount
global result


def get_variable(num):
    global i
    display.insert(i, num)
    i += 1


def multiply(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length


def get_area(unit):
    global area
    try:
        a = display.get()
        x = parser.expr(a).compile()
        area = eval(x)
        area = area * unit
        clear_all()
        display.insert(0, area)
    except Exception:
        clear_all()
        display.insert("Error")


def get_amount(rate):
    global area
    global amount
    amount = area * rate
    clear_all()
    display.insert(0, "$" + str(amount))


def clear_all():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


def give_discount():
    global amount
    try:
        a = float(display.get())
        disc = (a/100) * amount
        amount = amount - disc
        clear_all()
        display.insert(0, "$" + str(amount))
    except Exception:
        clear_all()
        display.insert(0, "Error")


def final_amount():
    global amount
    amount = int(amount)
    clear_all()
    display.insert(0, "Final amount is $" + str(amount))


# create entry widget
display = Entry(root)
display.grid(row=1, columnspan=8, sticky=W+E)


# adding buttons to the calc
Button(root, text="1", command=lambda: get_variable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variable(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_variable(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variable(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_variable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variable(9)).grid(row=4, column=2)

Button(root, text="*", command=lambda: multiply('*')).grid(row=2, column=3)
Button(root, text="M", command=lambda: get_area(10.7639)).grid(row=3, column=3)
Button(root, text="Inch", command=lambda: get_area(0.00694444)).grid(row=4, column=3)
Button(root, text="FT", command=lambda: get_area(1)).grid(row=5, column=3)

Button(root, text="Amount", command=lambda: get_amount(20)).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_variable(0)).grid(row=5, column=1)
Button(root, text="Discount %", command=lambda: give_discount()).grid(row=5, column=2)

Button(root, text="Final Amount",command=lambda: final_amount()).grid(row=6, column=1)
Button(root, text="A/C", command=lambda: clear_all()).grid(row=6, column=0)
Button(root, text="Undo", command=lambda: undo()).grid(row=6, column=2)
Button(root, text="Give Discount", command=lambda: clear_all()).grid(row=6, column=3)

root.mainloop()
