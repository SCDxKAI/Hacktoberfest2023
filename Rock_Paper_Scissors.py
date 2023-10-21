from random import choice

# Create a list of play options
t = ["Rock", "Paper", "Scissors"]

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # Assign a random play to the computer
    computer = choice(t)

    # Get the player's choice and make it case-insensitive
    player = input("Rock, Paper, Scissors? ").capitalize()

    # Check for a valid play
    if player in t:
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose! Paper covers Rock")
                computer_score += 1
            else:
                print("You win! Rock smashes Scissors")
                user_score += 1
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose! Scissors cut Paper")
                computer_score += 1
            else:
                print("You win! Paper covers Rock")
                user_score += 1
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose! Rock smashes Scissors")
                computer_score += 1
            else:
                print("You win! Scissors cut Paper")
                user_score += 1

        # Display the current scores
        print(f"User Score: {user_score}, Computer Score: {computer_score}")

        # Ask if the player wants to play another round
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    else:
        print("That's not a valid play. Check your spelling!")

print("Thanks for playing!")
