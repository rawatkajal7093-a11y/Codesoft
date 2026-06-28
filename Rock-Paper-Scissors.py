from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("650x650")
root.configure(bg = "#1e1e2e")
root.resizable(False, False)

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

emoji = {
    "Rock": "Rock",
    "Paper": "Paper",
    "Scissors": "Scissors"
}

title = Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Segoe UI", 24, "bold"),
    bg = "#1e1e2e",
    fg="#00E5FF"
)
title.pack(pady=20)

score_frame = Frame(root,  bg = "#1e1e2e")
score_frame.pack()

user_score_label = Label(
    score_frame,
    text="You : 0",
    font=("Segoe UI",18,"bold"),
    bg = "#1e1e2e",
    fg="white"
)
user_score_label.grid(row=0,column=0,padx=40)

computer_score_label = Label(
    score_frame,
    text="Computer : 0",
    font=("Segoe UI",18,"bold"),
    bg = "#1e1e2e",
    fg="white"
)
computer_score_label.grid(row=0,column=1,padx=40)

status_label = Label(
    root,
    text="Choose Your Move",
    font=("Segoe UI",20,"bold"),
    bg = "#1e1e2e",
    fg="#FFD54F"
)
status_label.pack(pady=20)

choice_frame = Frame(root,bg="#1e1e2e")
choice_frame.pack(pady=20)

user_choice_label = Label(
    choice_frame,
    text="You : ?",
    font=("Segoe UI",20),
    bg = "#1e1e2e",
    fg="white"
)
user_choice_label = Label(
    choice_frame,
    text="You: -",
    font=("Segoe UI", 18, "bold"),
    bg = "#1e1e2e",
    fg="white"
)

computer_choice_label = Label(
    choice_frame,
    text="Computer: -",
    font=("Segoe UI", 18, "bold"),
    bg = "#1e1e2e",
    fg="white"
)
def play(user_choice):
    global user_score, computer_score

    computer_choice_label = Label(
    choice_frame,
    text="Computer: -",
    font=("Segoe UI", 18, "bold"),
    bg = "#1e1e2e",
    fg="white"
)

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"You: {user_choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        status_label.config(text="It's a Draw!", fg="yellow")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1

        status_label.config(
            text="You Win!",
            fg="lightgreen"
        )

    else:
        computer_score += 1

        status_label.config(
            text="Computer Wins!",
            fg="red"
        )

    user_score_label.config(text=f"You: {user_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")

def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_score_label.config(text=" You : 0")
    computer_score_label.config(text="Computer : 0")

    user_choice_label.config(text=" You : ?")
    computer_choice_label.config(text="Computer : ?")

    status_label.config(
        text="Choose Your Move",
        fg="#F3C83D"
    )

button_frame = Frame(root, bg="#1e1e2e")
button_frame.pack(pady=40)


rock_btn = Button(
    button_frame,
    text="Rock",
    font=("Segoe UI", 16, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2",
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=15, pady=10)


paper_btn = Button(
    button_frame,
    text="Paper",
    font=("Segoe UI", 16, "bold"),
    bg="#2196F3",
    fg="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2",
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=15, pady=10)


scissors_btn = Button(
    button_frame,
    text="Scissors",
    font=("Segoe UI", 16, "bold"),
    bg="#FF9800",
    fg="white",
    width=12,
    height=2,
    relief="flat",
    cursor="hand2",
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=15, pady=10)


reset_btn = Button(
    root,
    text="Reset Game",
    font=("Segoe UI", 16, "bold"),
    bg="#F44336",
    fg="white",
    width=20,
    height=2,
    relief="flat",
    cursor="hand2",
    command=reset_game
)
reset_btn.pack(pady=30)

footer = Label(
    root,
    text="Made with Heart using Python Tkinter",
    font=("Segoe UI", 12),
    bg = "#1e1e2e",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=20)


def enter_green(e):
    rock_btn.config(bg="#66BB6A")

def leave_green(e):
    rock_btn.config(bg="#4CAF50")

rock_btn.bind("<Enter>", enter_green)
rock_btn.bind("<Leave>", leave_green)


def enter_blue(e):
    paper_btn.config(bg="#42A5F5")

def leave_blue(e):
    paper_btn.config(bg="#2196F3")

paper_btn.bind("<Enter>", enter_blue)
paper_btn.bind("<Leave>", leave_blue)


def enter_orange(e):
    scissors_btn.config(bg="#FFA726")

def leave_orange(e):
    scissors_btn.config(bg="#FF9800")

scissors_btn.bind("<Enter>", enter_orange)
scissors_btn.bind("<Leave>", leave_orange)


def enter_red(e):
    reset_btn.config(bg="#EF5350")

def leave_red(e):
    reset_btn.config(bg="#F44336")

reset_btn.bind("<Enter>", enter_red)
reset_btn.bind("<Leave>", leave_red)


root.mainloop()
