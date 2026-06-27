from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("360x560")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = StringVar()

entry = Entry(
    root,
    textvariable=expression,
    font=("Segoe UI", 24, "bold"),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    bd=0,
    justify="right"
)
entry.pack(fill=X, padx=15, pady=20, ipady=18)


def press(value):
    expression.set(expression.get() + str(value))


def clear():
    expression.set("")


def backspace():
    expression.set(expression.get()[:-1])


def calculate():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")


frame = Frame(root, bg="#1e1e1e")
frame.pack(padx=10, pady=10)

buttons = [
    ["AC", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for row in buttons:
    row_frame = Frame(frame, bg="#1e1e1e")
    row_frame.pack()

    for button in row:

        if button == "AC":
            bg = "#d32f2f"
            command = clear

        elif button == "⌫":
            bg = "#616161"
            command = backspace

        elif button == "=":
            bg = "#00c853"
            command = calculate

        elif button in ["+", "-", "*", "/", "%"]:
            bg = "#ff9800"
            command = lambda b=button: press(b)

        else:
            bg = "#424242"
            command = lambda b=button: press(b)

        Button(
            row_frame,
            text=button,
            command=command,
            font=("Segoe UI", 18, "bold"),
            bg=bg,
            fg="white",
            activebackground="#616161",
            activeforeground="white",
            relief="flat",
            bd=0,
            width=5,
            height=2,
            cursor="hand2"
        ).pack(side=LEFT, padx=6, pady=6)

root.mainloop()