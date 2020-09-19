from xgboost import XGBRegressor
from tkinter import *
from tkmacosx import Button
import parser
import math
from calc import *

root = Tk()
root.title("Tax Calculator")
i = 0
global age
global income


def get_age(num):
    global i
    display1.insert(i, num)
    i += 1


def get_income(num):
    global i
    display2.insert(i, num)
    i += 1


def clear_age():
    display1.delete(0, END)


def clear_income():
    display2.delete(0, END)


def undo_age():
    entire_string = display1.get()
    new_string = entire_string[:-1]
    clear_age()
    display1.insert(0, new_string)


def undo_income():
    entire_string = display2.get()
    new_string = entire_string[:-1]
    clear_income()
    display2.insert(0, new_string)


def calculate():
    global age
    global income
    age = int(display1.get())
    income = int(display2.get())
    clear_age()
    clear_income()
    display.insert(0, "$" + str(int(cal(age, income))) + " is your tax")


display = Entry(root)
display.grid(row=0, column=1, columnspan=5, sticky=W + E)

label = Label(text="Total Tax")
label.grid(row=0, column=0)

label1 = Label(text="Enter your age")
label1.grid(row=1, column=0)

display1 = Entry(root)
display1.grid(row=1, column=1, columnspan=5, sticky=W + E)

label2 = Label(text="Enter your income")
label2.grid(row=6, column=0)

display2 = Entry(root)
display2.grid(row=6, column=1, columnspan=5, sticky=W + E)

Button(text="1", command=lambda: get_age(1)).grid(row=2, column=0)
Button(text="2", command=lambda: get_age(2)).grid(row=2, column=1)
Button(text="3", command=lambda: get_age(3)).grid(row=2, column=2)

Button(text="4", command=lambda: get_age(4)).grid(row=3, column=0)
Button(text="5", command=lambda: get_age(5)).grid(row=3, column=1)
Button(text="6", command=lambda: get_age(6)).grid(row=3, column=2)

Button(text="7", command=lambda: get_age(7)).grid(row=4, column=0)
Button(text="8", command=lambda: get_age(8)).grid(row=4, column=1)
Button(text="9", command=lambda: get_age(9)).grid(row=4, column=2)

Button(text="1", command=lambda: get_income(1)).grid(row=7, column=0)
Button(text="2", command=lambda: get_income(2)).grid(row=7, column=1)
Button(text="3", command=lambda: get_income(3)).grid(row=7, column=2)

Button(text="4", command=lambda: get_income(4)).grid(row=8, column=0)
Button(text="5", command=lambda: get_income(5)).grid(row=8, column=1)
Button(text="6", command=lambda: get_income(6)).grid(row=8, column=2)

Button(text="7", command=lambda: get_income(7)).grid(row=9, column=0)
Button(text="8", command=lambda: get_income(8)).grid(row=9, column=1)
Button(text="9", command=lambda: get_income(9)).grid(row=9, column=2)

Button(text="0", command=lambda: get_age(0)).grid(row=5, column=1)
Button(text="0", command=lambda: get_income(0)).grid(row=10, column=1)
Button(text="Calculate Tax", command=lambda: calculate()).grid(row=11, column=1)

Button(text="Undo", command=lambda: undo_age()).grid(row=5, column=0)
Button(text="Undo", command=lambda:undo_income()).grid(row=10, column=0)

Button(text="AC", command=lambda: clear_age()).grid(row=5, column=2)
Button(text="AC", command=lambda: clear_income()).grid(row=10, column=2)

root.mainloop()
