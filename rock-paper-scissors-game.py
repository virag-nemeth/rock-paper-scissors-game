import random

# Define the possible actions
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possible_actions = [rock, paper, scissors]

# Initialize scores
player_score = 0
computer_score = 0

print("Welcome to the Rock-Paper-Scissors Game!")

# Start the game loop
play_again = "y"
while play_again.lower() == "y":
    # Get user input
    user_action = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

    # Validate input
    if not user_action.isdigit() or int(user_action) not in [0, 1, 2]:
        print("Invalid input! Please enter 0, 1, or 2.")
    else:
        user_action = int(user_action)

        # Computer's random choice
        computer_action = random.randint(0, 2)

        # Display choices
        print(f"\nYou chose:\n{possible_actions[user_action]}")
        print(f"Computer chose:\n{possible_actions[computer_action]}")

        # Game logic to determine the winner
        if user_action == computer_action:
            print("It's a draw!")
        elif user_action == 0 and computer_action == 2:
            print("Rock smashes scissors! You win!")
            player_score += 1
        elif user_action == 1 and computer_action == 0:
            print("Paper covers rock! You win!")
            player_score += 1
        elif user_action == 2 and computer_action == 1:
            print("Scissors cuts paper! You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        # Display the current score
        print(f"\nScore: Player {player_score} - Computer {computer_score}")

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (y/n): ")

print("\nThanks for playing! Final score:")
print(f"Player: {player_score} - Computer: {computer_score}")
