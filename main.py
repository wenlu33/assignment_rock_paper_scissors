import random
possible_actions = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
max_score = 3
round = 1

while user_score < max_score and computer_score:
    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ")
        user_action = user_action.upper()
        if user_action in possible_actions:
            break
        print('Invalid input. Please try again.')

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!")
            user_score += 1
        else:
            print("You lose.")
            computer_score += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
            user_score += 1
        else:
            print("You lose.")
            computer_score += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
            user_score += 1
        else:
            print("You lose.")
            computer_score += 1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

