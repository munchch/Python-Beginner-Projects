import random
import sys

while True:
    the_answer = random.randint(0, 20)
    health_bar = 3
    print("I have picked a number between 0 and 20. Can you guess it? You have 3 rights to guess!")
    
    while health_bar > 0:
        try:
            user_guess = input("Enter your guess:")
            
            if user_guess.lower() == "no":
                print("Exiting Game")
                sys.exit()
            
            user_guess = int(user_guess)
            
            if user_guess == the_answer:
                print("Congratulations! You guessed it right")
                play_again = input("Would you like to play again? (yes/no): ")
               
                if play_again.lower() != "yes":
                   
                   print("Thanks for playing!")
                   sys.exit()
                   
                else:
                   print("Starting a new game...\n")
        
            elif user_guess > the_answer:
                print("You should go lower")
                health_bar-=1
            
            else:
                print("You should go higher")
                health_bar-=1
                
            print("Remaining guesses: "+ str(health_bar))
            
            if health_bar == 0:
                
                print("Game Over! The correct number was: "+ str(the_answer))
                
                play_again = input("Would you like to play again? (yes/no): ")
               
                if play_again.lower() != "yes":
                   
                   print("Thanks for playing!")
                   sys.exit()
                   
                else:
                   print("Starting a new game...\n")

        except ValueError:
           print("Please enter a valid integer or 'no' to quit.")
                
                
