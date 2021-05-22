# Rock Paper Scissors by Arvind Narayanan
import random
import time


def start():
    actions = ["rock", "paper", "scissors"]
    global computer_choice, player_choice
    computer_choice = random.choice(actions)
    print("Welcome to Rock Paper Scissors!")
    time.sleep(1)
    player_choice = input("What do you choose, rock, paper, or scissors? ")


def decide_winner():
    global player_choice, computer_choice
    if player_choice == computer_choice:
        print("Both players picked the same choice. It's a tie!")
    elif player_choice in ["rock", "r", "Rock", "ROCK"]:
        if computer_choice == "scissors":
            print("Rock smashes scissors. Yay! You are the winner")
        elif computer_choice == "paper":
            print("Paper covers Rock. Your opponent has won!")
        else:
            print("Both players picked the same choice. It's a tie!")
    elif player_choice in ["s", "scissors", "Scissors"]:
        if computer_choice == "paper":
            print("Scissors cut Paper. Yay! You are the winner")
        elif computer_choice == "rock":
            print("Rock smashes scissors. Your opponent has won!")
        else:
            print("Both players picked the same choice. It's a tie!")
    elif player_choice in ["p", "paper", "Paper"]:
        if computer_choice == "rock":
            print("Paper covers Rock. Yay! You are the winner")
        elif computer_choice == "scissors":
            print("Scissors cuts Paper. Your opponent has won!")
        else:
            print("Both players picked the same choice. It’s a tie!")
    else:
        player_choice = input("Please enter rock, paper, or scissors: ")
        decide_winner()


def game():
    start()
    print("You chose " + player_choice + "! Your opponent chose " + computer_choice + "!")
    time.sleep(1)
    decide_winner()
    time.sleep(1)
    play_again = input("Do you want to play again? ")
    if play_again in ["Yes", "yes", "yup", "of course", "yeah"]:
        game()
    else:
        print("Ok, Bye! Hope you come again!")
        time.sleep(1.3)
        quit()


print("Rock Paper Scissors, by Arvind Narayanan")
time.sleep(1)
game()
