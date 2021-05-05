# My own idea for a calculator
#floating point input only works by using the keyboard.

from tkinter import *

root = Tk()
root.title("Calculator")


output = Entry(root, width=50)
output.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

term = []

# Commands for number buttons
def click_1():
    output.insert(len(output.get()), "1")
def click_2():
    output.insert(len(output.get()), "2")
def click_3():
    output.insert(len(output.get()), "3")
def click_4():
    output.insert(len(output.get()), "4")
def click_5():
    output.insert(len(output.get()), "5")
def click_6():
    output.insert(len(output.get()), "6")
def click_7():
    output.insert(len(output.get()), "7")
def click_8():
    output.insert(len(output.get()), "8")
def click_9():
    output.insert(len(output.get()), "9")
def click_0():
    output.insert(len(output.get()), "0")
    
# Operations
def click_plus():
    term.append(output.get())
    output.delete(0, len(output.get()))
    term.append("+")
def click_minus():
    term.append(output.get())
    output.delete(0, len(output.get()))
    term.append("-")
def click_times():
    term.append(output.get())
    output.delete(0, len(output.get()))
    term.append("*")
def click_divided():
    term.append(output.get())
    output.delete(0, len(output.get()))
    term.append("/")
def click_equal():
    try:
        term.append(output.get())
        output.delete(0, len(output.get()))
        stringterm = "".join(term)
        result = eval(stringterm)
        output.insert(0, result)
        term.clear()
    except:
        click_clear()
def click_clear():
    term.clear()
    output.delete(0, len(output.get()))
            
            
            
# Buttons
button_1 = Button(root, text="1", command=click_1, padx=10, pady=10)
button_2 = Button(root, text="2", command=click_2, padx=10, pady=10)
button_3 = Button(root, text="3", command=click_3, padx=10, pady=10)
button_4 = Button(root, text="4", command=click_4, padx=10, pady=10)
button_5 = Button(root, text="5", command=click_5, padx=10, pady=10)
button_6 = Button(root, text="6", command=click_6, padx=10, pady=10)
button_7 = Button(root, text="7", command=click_7, padx=10, pady=10)
button_8 = Button(root, text="8", command=click_8, padx=10, pady=10)
button_9 = Button(root, text="9", command=click_9, padx=10, pady=10)
button_0 = Button(root, text="0", command=click_0, padx=10, pady=10)
button_plus = Button(root, text="+", command=click_plus, padx=10, pady=10)
button_minus = Button(root, text="-", command=click_minus, padx=10, pady=10)
button_times = Button(root, text="*", command=click_times, padx=10, pady=10)
button_divided = Button(root, text="/", command=click_divided, padx=10, pady=10)
button_equal = Button(root, text="=", command=click_equal, padx=10, pady=10, bg="lightgrey")
button_clear = Button(root, text="CLEAR", command=click_clear, padx=30, pady=10)

# Placing the buttons in the grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_plus.grid(row=4, column=2)
button_equal.grid(row=4, column=0)
button_minus.grid(row=5, column=0)
button_times.grid(row=5, column=1)
button_divided.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()
