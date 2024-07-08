from colorama import Fore, Style
import inquirer
import random

rock = f"{Fore.BLUE}rock{Style.RESET_ALL}"
paper = f"{Fore.MAGENTA}paper{Style.RESET_ALL}"
scissors = f"{Fore.YELLOW}scissors{Style.RESET_ALL}"

def get_user_choice():
    questions = [
        inquirer.List("choice",
                      message=f"{Fore.GREEN}Enter your choice{Style.RESET_ALL}",
                      choices=[rock, paper, scissors]
        ),
    ]
    answers = inquirer.prompt(questions)
    return answers["choice"]

def get_computer_choice():
    return random.choice([rock, paper, scissors])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == rock and computer_choice == scissors) or \
         (user_choice == paper and computer_choice == rock) or \
         (user_choice == scissors and computer_choice == paper):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0
    ties = 0

    again_question = [
        inquirer.List("play",
                      message=f"{Fore.WHITE}Do you want to play again?{Style.RESET_ALL}",
                      choices=[f"{Fore.GREEN}yes{Style.RESET_ALL}", f"{Fore.RED}no{Style.RESET_ALL}"]
        ),
    ]

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        elif result == "It's a tie!":
            ties += 1

        play_again = inquirer.prompt(again_question)["play"]
        if play_again != f"{Fore.GREEN}yes{Style.RESET_ALL}":
            break

    print(f"\nFinal score: You {user_score} - Computer {computer_score} - Ties {ties}")

play_game()