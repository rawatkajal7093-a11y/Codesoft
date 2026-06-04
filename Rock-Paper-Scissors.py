import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]
print("ROCK PAPER SCISSORS GAME")

while True:
    print("Choose: Rock, Paper, or Scissors")
    user_choice = input("Your choice: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")
        user_score += 1    