import random

positive_responses = ["yes", "yea", "yeah", "yup", "ok", "sure", "ok then lets do it", "Nope", "NAH HELL NO"]

negative_responses = ["bad word", ":))(())(())(())(())"]

name = input("What is your name? Enter it here: ")
print(f"Hello, {name}!")

gameapprov = input(f"Do you want to play a game, {name}? [yes or no] ").lower()

if gameapprov in positive_responses:
    print("Okay! Let's play rock paper scissors.")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Rock, Paper, or Scissors? (or type 'quit' to stop): ").lower()
        
        if player_choice == "quit":
            print(f"Thanks for playing! Goodbye, {name}!")
            break
           
        if player_choice in negative_responses:
          print(":(")
          continue

        if player_choice not in choices:
            print("Uhh... try again!")
            continue
        
        computer_choice = random.choice(choices)
        print(f"I choose {computer_choice.capitalize()}!")
        
        # Makes the robot say "You win!", "I win!", or "Its a tie!"
        if player_choice == computer_choice:
            print(f"{name}, Guess what... It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print(f"{name}, you win!")
        else:
            print("The robot wins!")
            
elif gameapprov == "no":
    print("Okay, bye!")
else:
    print("Please answer with 'yes' or 'no'.")
