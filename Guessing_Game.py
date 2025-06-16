
"""
Guess the Number Game
Author: Arda
Description: A simple terminal-based game where the player has 3 chances to guess a number between 0 and 20.
"""

import random #Will be used to pick random number between 0-20
import sys #Will be used the terminate the game when it is needed

while True:
    the_answer = random.randint(0, 20) #picking a number randomly
    health_bar = 3 
    print("I have picked a number between 0 and 20. Can you guess it? You have 3 rights to guess!")
    
    while health_bar > 0: #the game carry on if player has more than zero health bar
        try:
            user_guess = input("Enter your guess:")
            
            if user_guess.lower() == "no": #User can log out by texting no
                print("Exiting Game")
                sys.exit()
            
            user_guess = int(user_guess)
            
            if user_guess == the_answer: #if player can guess the number player wins
                print("Congratulations! You guessed it right")
                play_again = input("Would you like to play again? (yes/no): ") #request for a rematch
               
                if play_again.lower() != "yes":
                   
                   print("Thanks for playing!")
                   sys.exit()
                   
                else:
                   print("Starting a new game...\n")
        
            elif user_guess > the_answer: 
                print("You should go lower") #if the guessed number is higher than the answer advices player to guess lower
                health_bar-=1
            
            else:
                print("You should go higher") #if the guessed number is lower than the answer advices player to guess higher
                health_bar-=1
                
            print("Remaining guesses: "+ str(health_bar)) #informing about remaining health bars
            
            if health_bar == 0: #if player runs out of health bars before guessing terminates the game
                
                print("Game Over! The correct number was: "+ str(the_answer))
                
                play_again = input("Would you like to play again? (yes/no): ")
               
                if play_again.lower() != "yes":
                   
                   print("Thanks for playing!")
                   sys.exit()
                   
                else:
                   print("Starting a new game...\n")

        except ValueError:
           print("Please enter a valid integer or 'no' to quit.")
                
                
