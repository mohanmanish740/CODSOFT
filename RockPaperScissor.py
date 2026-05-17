import random

user_score_counter = 0
computer_score_counter = 0

game_choices_list = ["rock", "paper", "scissors"]

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choose: rock, paper, or scissors")

    user_choice_input = input("Your choice: ").lower()

    if user_choice_input not in game_choices_list:
        print("Invalid choice! Try again.")
        continue

    computer_choice_generated = random.choice(game_choices_list)

    print("You chose:", user_choice_input)
    print("Computer chose:", computer_choice_generated)

    if user_choice_input == computer_choice_generated:
        print("Result: It's a tie!")

    elif (
        (user_choice_input == "rock" and computer_choice_generated == "scissors") or
        (user_choice_input == "scissors" and computer_choice_generated == "paper") or
        (user_choice_input == "paper" and computer_choice_generated == "rock")
    ):
        print("Result: You win!")
        user_score_counter += 1

    else:
        print("Result: You lose!")
        computer_score_counter += 1

    print("Score -> You:", user_score_counter, "| Computer:", computer_score_counter)

    play_again_choice = input("Play again? (yes/no): ").lower()

    if play_again_choice != "yes":
        print("Final Score -> You:", user_score_counter, "| Computer:", computer_score_counter)
        print("Thanks for playing!")
        break