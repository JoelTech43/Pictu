import tkinter as tk
import math
equation = ""

window = tk.Tk()
window.title("Calculator")
def greet():
    namein = entry.get()
    name2 = "Hello, " + namein
    greeting["text"]=name2

def one():
    global equation
    equation += "1"
    answer["text"] = str(equation)
def two():
    global equation
    equation += "2"
    answer["text"] = str(equation)
def three():
    global equation
    equation += "3"
    answer["text"] = str(equation)
def four():
    global equation
    equation += "4"
    answer["text"] = str(equation)
def five():
    global equation
    equation += "5"
    answer["text"] = str(equation)
def six():
    global equation
    equation += "6"
    answer["text"] = str(equation)
def seven():
    global equation
    equation += "7"
    answer["text"] = str(equation)
def eight():
    global equation
    equation += "8"
    answer["text"] = str(equation)
def nine():
    global equation
    equation += "9"
    answer["text"] = str(equation)
def zero():
    global equation
    equation += "0"
    answer["text"] = str(equation)
def add():
    global equation
    equation += "+"
    answer["text"] = str(equation)
def sub():
    global equation
    equation += "-"
    answer["text"] = str(equation)
def multi():
    global equation
    equation += "*"
    answer["text"] = str(equation)
def divide():
    global equation
    equation += "/"
    answer["text"] = str(equation)
def pow():
    global equation
    equation += "**"
    answer["text"] = str(equation)
def cancel():
    global equation
    equation = ""
    answer["text"] = str(equation)
def back():
    try:
        global equation
        if equation[-1] == "*" and equation [-2] == "*":
            equation = equation[:-2]
        else:
            equation = equation[:-1]
        answer["text"] = str(equation)
    except IndexError:
        pass
def equal():
    try:
        global equation
        equation = str(eval(equation))
        answer["text"] = equation
    except SyntaxError:
        answer["text"] = "Error"

window.geometry("500x455")

answer = tk.Label(window, text="Welcome",borderwidth=2, width=500,height=3,bg="#565656", font=("Arial", 25),fg="#FFFFFF")
answer.pack(padx=0)

buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=one)
btn1.grid(column=0,row=1,sticky=tk.E+tk.W)
btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=two)
btn2.grid(column=1,row=1,sticky=tk.E+tk.W)
btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=three)
btn3.grid(column=2,row=1,sticky=tk.E+tk.W)
btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=four)
btn4.grid(column=0,row=2,sticky=tk.E+tk.W)
btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=five)
btn5.grid(column=1,row=2,sticky=tk.E+tk.W)
btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=six)
btn6.grid(column=2,row=2,sticky=tk.E+tk.W)
btn7 = tk.Button(buttonFrame, text="7", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=seven)
btn7.grid(column=0,row=3,sticky=tk.E+tk.W)
btn8 = tk.Button(buttonFrame, text="8", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=eight)
btn8.grid(column=1,row=3,sticky=tk.E+tk.W)
btn9 = tk.Button(buttonFrame, text="9", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=nine)
btn9.grid(column=2,row=3,sticky=tk.E+tk.W)
btn10 = tk.Button(buttonFrame, text="0", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=zero)
btn10.grid(column=0,row=4,sticky=tk.E+tk.W, columnspan=3)
btn11 = tk.Button(buttonFrame, text="+", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=add)
btn11.grid(column=3,row=0,sticky=tk.E+tk.W)
btn12 = tk.Button(buttonFrame, text="-", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=sub)
btn12.grid(column=3,row=1,sticky=tk.E+tk.W)
btn13 = tk.Button(buttonFrame, text="*", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=multi)
btn13.grid(column=3,row=2,sticky=tk.E+tk.W)
btn14 = tk.Button(buttonFrame, text="/", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=divide)
btn14.grid(column=3,row=3,sticky=tk.E+tk.W)
btn15 = tk.Button(buttonFrame, text="AC", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=cancel)
btn15.grid(column=0,row=0,sticky=tk.E+tk.W)
btn17 = tk.Button(buttonFrame, text="^", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=pow)
btn17.grid(column=1,row=0,sticky=tk.E+tk.W)
btn18 = tk.Button(buttonFrame, text="<<", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=back)
btn18.grid(column=2,row=0,sticky=tk.E+tk.W)
btn19 = tk.Button(buttonFrame, text="=", font=("Arial", 25), bg="#040273", fg="#FFFFFF", command=equal)
btn19.grid(column=3,row=4,sticky=tk.E+tk.W)

buttonFrame.pack(fill="x")
window.mainloop()
