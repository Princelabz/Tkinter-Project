import tkinter as tk

r = tk.Tk()
r.title('Calculator')

entry = tk.Entry(r, width=20, borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "NOt divisible by zero")

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+' , 1 ,3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-' , 2 ,3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*' , 3 ,3),
    ('C', 4, 0), ('0', 4, 1), ('=' , 4 ,2), ('/' , 4 ,3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(r, text=text, width=10, command=button_equal).grid(row=row, column=col, padx=2, pady=2)
    elif text == "C":
        tk.Button(r, text=text, width=10, command=button_clear).grid(row=row, column=col, padx=2, pady=2)
    else:
        tk.Button(r, text=text, width=10, command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=2, pady=2)

r.mainloop()

