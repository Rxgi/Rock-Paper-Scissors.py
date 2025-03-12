import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def user_choice():
    while True:
        choice = input("Enter Rock, Paper or Scissors: ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Please enter either Rock, Paper or Scissors")

def conclude_choices(player, computer):
    if player == computer:
        print("It is a Tie")
    elif player == "rock" and computer == "scissors":
        print("You Win")
    elif player == "scissors" and computer == "paper":
        print("You Win")
    elif player == "paper" and computer == "rock":
        print("You Win")
    else:
        print("You Lose")

def play_game():
    play_user = user_choice()
    play_computer = computer_choice()
    print(f"The Computer Chose {play_computer}")
    conclude_choices(play_user, play_computer)

play_game()