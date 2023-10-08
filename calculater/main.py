import tkinter as tk
app = tk.Tk()
app.title("calculator")
entry =tk.Entry(app,width=20)
entry.grid(row= 0,colum=0,colimnspan=4)
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "错误")
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button_text in button_texts:
    if button_text == "=":
        btn = tk.Button(app, text=button_text, width=5, command=calculate)
    elif button_text == "C":
        btn = tk.Button(app, text=button_text, width=5, command=clear)
    else:
        btn = tk.Button(app, text=button_text, width=5, command=lambda x=button_text: button_click(x))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
app.mainloop()
