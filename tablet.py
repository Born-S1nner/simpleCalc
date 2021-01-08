from tkinter import *

window = Tk()
expression = ""

def input_number(number, equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def clear_input_field(equation):
    global expression
    expression = ""
    equation.set("Enter the Expression")

def evaluate(equation):
    global expression
    try: 
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        expression = ""

def mainCalc():
    window.title("SimpleCalc")
    window.geometry("325x175")
    Label(window, text="Simple_Calculator").grid(row=0)

    equation = StringVar()
    input_field = Entry(window, textvariable=equation)
    input_field.place(height=100)
    input_field.grid(row=1, columnspan=4, ipadx=100, ipady=5)
    equation.set("Enter the Expression")

    _1 = Button(window, text="1", command=lambda: input_number(1, equation))
    _1.grid(row=2, column=0)

    _2 = Button(window, text="2", command=lambda: input_number(2, equation))
    _2.grid(row=3, column=0)

    _3 = Button(window, text="3", command=lambda: input_number(3, equation))
    _3.grid(row=2, column=1)

    _4 = Button(window, text="4", command=lambda: input_number(4, equation))
    _4.grid(row=3, column=1)

    add = Button(window, text="+", command=lambda: input_number('+', equation))
    add.grid(row=4)

    equal = Button(window, text="=", command=lambda: evaluate(equation))
    equal.grid(row=5, columnspan=6)

    clear = Button(window, text='Clear', command=lambda: clear_input_field(equation))
    clear.grid(row=5, columnspan=3)

    window.mainloop()

if __name__ == '__main__':
    mainCalc()