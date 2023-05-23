from tkinter import *

math_text = ""
answer = 0

def func_0():
    global math_text
    math_text += "0"
    label.config(text=math_text)

def func_1():
    global math_text
    math_text += "1"
    label.config(text = math_text)

def func_2():
    global math_text
    math_text += "2"
    label.config(text = math_text)

def func_3():
    global math_text
    math_text += "3"
    label.config(text = math_text)

def func_4():
    global math_text
    math_text += "4"
    label.config(text = math_text)

def func_5():
    global math_text
    math_text += "5"
    label.config(text = math_text)

def func_6():
    global math_text
    math_text += "6"
    label.config(text = math_text)

def func_7():
    global math_text
    math_text += "7"
    label.config(text = math_text)

def func_8():
    global math_text
    math_text += "8"
    label.config(text = math_text)

def func_9():
    global math_text
    math_text += "9"
    label.config(text = math_text)

def func_division():
    global math_text

    math_text += "/"
    label.config(text = math_text)

def func_multiplication():
    global math_text
    math_text += "*"
    label.config(text = math_text)

def func_minus():
    global math_text
    math_text += "-"
    label.config(text = math_text)

def func_plus():
    global math_text
    math_text += "+"
    label.config(text = math_text)

def func_dote():
    global math_text
    math_text += "."
    label.config(text = math_text)

def func_equal():
    global answer
    global math_text
    try:
        answer = eval(str(math_text))
        label.config(text = eval(math_text))
    except SyntaxError:
        label.config(text = "Error try again")
    math_text = ""

def backspace():
    global math_text
    math_text = math_text[0:-1]
    label.config(text = math_text)

def ac():
    global math_text
    math_text = ""
    label.config(text = math_text)

def ans():
    global answer
    global math_text
    math_text += str(answer)
    label.config(text = math_text)

def brackets1():
    global math_text
    math_text += "("
    label.config(text = math_text)

def brackets2():
    global math_text
    math_text += ")"
    label.config(text = math_text)

window = Tk()
window.title("Calculator")
photo = PhotoImage(file = "images.png")
window.iconphoto(False, photo)

x = 10
y = 3

label = Label(text = "Math exercise", width = 27, height = y, font = 16)
label.grid(row = 1, column = 1, columnspan = 4)

button_backspace = Button(text = "backspace", width = 22, height = y, command = backspace)
button_backspace.grid(row = 2, column = 1, columnspan = 2)

button_ac = Button(text = "AC", width = 22, height = y, command = ac)
button_ac.grid(row = 2, column = 3, columnspan = 4)

button_ans = Button(text = "ANS", width = 22, height = y, command = ans)
button_ans.grid(row = 3, column = 1, columnspan = 2)

button_brackets1 = Button(text = "(", width = x, height = y, command = brackets1)
button_brackets1.grid(row = 3, column = 3)

button_brackets2 = Button(text = ")", width = x, height = y, command = brackets2)
button_brackets2.grid(row = 3, column = 4)

button_7 = Button(text = "7", width = x, height = y, command = func_7)
button_7.grid(row = 4, column = 1)

button_8 = Button(text = "8", width = x, height = y, command = func_8)
button_8.grid(row = 4, column = 2)

button_9 = Button(text = "9", width = x, height = y, command = func_9)
button_9.grid(row = 4, column = 3)

button_division = Button(text = "/", width = x, height = y, command = func_division)
button_division.grid(row = 4, column = 4)

button_4 = Button(text = "4", width = x, height = y, command = func_4)
button_4.grid(row = 5, column = 1)

button_5 = Button(text = "5", width = x, height = y, command = func_5)
button_5.grid(row = 5, column = 2)

button_6 = Button(text = "6", width = x, height = y, command = func_6)
button_6.grid(row = 5, column = 3)

button_multiplication = Button(text = "*", width = x, height = y, command = func_multiplication)
button_multiplication.grid(row = 5, column = 4)

button_1 = Button(text = "1", width = x, height = y, command = func_1)
button_1.grid(row = 6, column = 1)

button_2 = Button(text = "2", width = x, height = y, command = func_2)
button_2.grid(row = 6, column = 2)

button_3 = Button(text = "3", width = x, height = y, command = func_3)
button_3.grid(row = 6, column = 3)

button_minus = Button(text = "-", width = x, height = y, command = func_minus)
button_minus.grid(row = 6, column = 4)

button_0 = Button(text = "0", width = x, height = y, command = func_0)
button_0.grid(row = 7, column = 1)

button_dote = Button(text = ".", width = x, height = y, command = func_dote)
button_dote.grid(row = 7, column = 2)

button_equal = Button(text = "=", width = x, height = y, command = func_equal)
button_equal.grid(row = 7, column = 3)

button_plus = Button(text = "+", width = x, height = y, command = func_plus)
button_plus.grid(row = 7, column = 4)

window.mainloop()







