#stone paper scissor
import random


def does_computer_kill(computer_choice, user_choice):
    return dict_kills[computer_choice] == user_choice

def play_round():
    choice_computer = random.choice(choices)
    user_choice = input("Please enter your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice.")
        return
    print("You chose {}".format(user_choice))
    print("Computer chose {}".format(choice_computer))
    if user_choice == choice_computer:
        print("Tie")
        pass
    else:
        if does_computer_kill(choice_computer, user_choice):
            print("Computer wins!")
            pass
        else:
            print("User wins!")
            pass

def main():
    try:
        rounds = input("How many rounds would you like to play? ")
        for r in range(int(rounds)):
            play_round()
    except ValueError as ve:
        print("Use NUMBERS ONLY for Rounds ", ve)
    finally:
        print("Thank you for playing, Make sure to play again.")

choices = ("stone", "paper", "scissor")

dict_kills = {"stone": "scissor",
              "paper": "stone",
              "scissor": "paper"}

if __name__ == "__main__":
    main()