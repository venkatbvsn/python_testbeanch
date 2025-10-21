import tkinter as tk

window = tk.Tk()
window.title("Basic Calculator")
window.geometry('275x400')

# Entry Box
entry = tk.Entry(window, width=43, borderwidth=5)
entry.place(x=0, y=0)

# Buttons
def click_fn(num):
    entry_text = entry.get()
    if entry_text.startswith('invalid'):
        entry_text = ''
    entry.delete(0, tk.END)
    entry.insert(0,str(entry_text)+str(num))
button = tk.Button(window, text='1', width=12, command= lambda :click_fn(1))
button.place(x=10, y=60)

button = tk.Button(window, text='2', width=12, command= lambda :click_fn(2))
button.place(x=80, y=60)

button = tk.Button(window, text='3', width=12, command= lambda :click_fn(3))
button.place(x=170, y=60)

button = tk.Button(window, text='4', width=12, command= lambda :click_fn(4))
button.place(x=10, y=120)

button = tk.Button(window, text='5', width=12, command= lambda :click_fn(5))
button.place(x=80, y=120)

button = tk.Button(window, text='6', width=12, command= lambda :click_fn(6))
button.place(x=170, y=120)

button = tk.Button(window, text='7', width=12, command= lambda :click_fn(7))
button.place(x=10, y=180)

button = tk.Button(window, text='8', width=12, command= lambda :click_fn(8))
button.place(x=80, y=180)

button = tk.Button(window, text='9', width=12, command= lambda :click_fn(9))
button.place(x=170, y=180)

button = tk.Button(window, text='0', width=12, command= lambda :click_fn(0))
button.place(x=80, y=240)

n1 = 0
math_operator = "none"

def add():
    global n1
    global math_operator
    n1_str = entry.get()
    if n1_str:
        n1 = int(n1_str)
    else:
        n1 = 0
    math_operator = "add"
    entry.delete(0, tk.END)
button = tk.Button(window, text='+', width=12, command=add)
button.place(x=10, y=300)

def sub():
    global n1
    global math_operator
    n1_str = entry.get()
    if n1_str:
        n1 = int(n1_str)
    else:
        n1 = 0
    math_operator = "sub"
    entry.delete(0, tk.END)

button = tk.Button(window, text='-', width=12, command=sub)
button.place(x=80, y=300)

def mul():
    global n1
    global math_operator
    n1_str = entry.get()
    if n1_str:
        n1 = int(n1_str)
        math_operator = "mul"
        entry.delete(0, tk.END)
    else:
        n1 = 0
        math_operator = "none"
        entry.delete(0, tk.END)
        entry.insert(0, 'invalid input')
button1 = tk.Button(window, text='*', width=12, command=mul)
button1.place(x=170, y=300)

def dev():
    global n1
    global math_operator
    n1_str = entry.get()
    if n1_str:
        n1 = int(n1_str)
        math_operator = "dev"
        entry.delete(0, tk.END)
    else:
        n1 = 0
        math_operator = "none"
        entry.delete(0, tk.END)
        entry.insert(0, 'invalid input')
button = tk.Button(window, text='/', width=12, command=dev)
button.place(x=10, y=360)

def equal():
    global n1
    global math_operator
    n2_str = entry.get()
    if n2_str:
        n2 = int(n2_str)
        if math_operator == 'add':
            result = n1 + n2
        elif math_operator == 'sub':
            result = n1 - n2
        elif math_operator == 'mul':
            result = n1 * n2
        elif math_operator == 'dev':
            if n2 == 0:
                result = 'invalid input'
            else:
                result = n1 // n2
        elif math_operator == 'none':
            result = 'invalid input'
    else:
        result = 'invalid input'
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
    n1 = 0
    math_operator = 'none'

button = tk.Button(window, text='=', width=12, command=equal)
button.place(x=80, y=360)

def clear():
    global n1
    global math_operator
    entry.delete(0, tk.END)
    n1 = 0
    math_operator = 'none'
button = tk.Button(window, text='clear', width=12, command=clear)
button.place(x=170, y=360)

# Mainloop
window.mainloop()