#A simple Rock, Paper, Scissors game in Python using basic concepts like loops, conditions, and randomization. The user plays against the computer, scores are tracked, and invalid inputs are handled. Players can quit anytime by pressing 'q'. A fun beginner-friendly project to practice Python fundamentals
import random #import random module
#Welcome note
print("Welcome to rock, paper and scissor game")
#choices declaration
choices=["rock", "paper", "scissors"]
#score counter
user_score = 0
computer_score = 0
#while loop for invalid and valid choice
while True:
    user_choice = input("Please select rock,paper and scissor or press q to quit the game: ")
#choice to to quit program 
    if user_choice == "q":
        print("Thank you for playing the game")
        print("User score: ",user_score, "Computer Score: ", computer_score)
    break
#Invalid choice code
    if user_choice not in choices:
        print("Invalid choice") 
    continue
#code for computer choice
computer_choice = random.choice(choices)
print("Computer choice is: ", computer_choice)
if user_choice == computer_choice :
    print("It's a tie")
elif(user_choice == "rock" and computer_choice == "scissor")or\
    (user_choice == "paper" and computer_choice == "rock")or\
    (user_choice == "scissor" and computer_choice == "paper"): 
        print("You have won")
        user_score += 1
else:
    print("You have lost!")
    computer_score += 1    
    exit()
print("User score: ",user_score, "Computer Score: ", computer_score)