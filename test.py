#rock paper scissors game
import random
user_score = 0
computer_score = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("type Rock/Paper/Scissors or q for quit:" ).lower()
    if user_input == 'q':
      break
    if user_input not in options:
      print("invalid input, try again" )
      continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    if user_input == "rock" and computer_pick == "scissors":
        print("you won" )
        user_score += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you win")
        user_score += 1   
    elif user_input == "paper" and computer_pick == "rock":
        print("you win")
        user_score += 1
    else:
        print("you lost")
        computer_score += 1
    print("You won", user_score, "times.")
    print("The computer won", computer_score, "times.")

print("Goodbye!")

         