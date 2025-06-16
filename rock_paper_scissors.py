"""
A Simple Rock-Paper-Scissors Game
Author: Arda
Description: A simple Python implementation of the classic Rock-Paper-Scissors game.  
"""


import random # used to randomize the answer of the computer

while True: # used to loop the round
    
    computers_score= 0
    users_score= 0 
    
    while computers_score < 3 and users_score < 3: # used to make game only carry on if no one has won
        
        computers_choice= random.choice(["rock", "paper", "scissors"]) # made computer choose randomly

        users_choice= input("\nChoose one of them! ROCK, PAPER, SCISSORS!: ").lower() # used to take request from the user
     
        if users_choice not in ["rock", "paper", "scissors"]: # ensuring whether the user entered input in correct format
            print("Please pick rock, paper or scissors")
            continue
        
        
        # analysing draw situation
        if users_choice == computers_choice: 
            print("Computer chose "+ computers_choice + " and you chose "+ users_choice + " DRAW!")
            
       
        # analyzing only the situations which computer wins
        elif (  
                users_choice == "rock" and computers_choice == "paper" 
            or users_choice == "paper" and computers_choice == "scissors" 
            or users_choice == "scissors" and computers_choice == "rock"
            ):
            print("Computer chose "+ computers_choice + " and you chose "+ users_choice + " YOU LOST!")
            computers_score+=1
        
        # we have already analysed draw and defeat situations so rest is victory (pun intented)    
        else: 
            print("Computer chose "+ computers_choice + " and you chose "+ users_choice + " YOU WON!")
            users_score+=1
            
        # a simple score table
        print("YOUR SCORE: " + str(users_score) + "     COMPUTER's SCORE: " + str(computers_score))
        
    # announcing the results
    if computers_score < users_score:
        print ("\n!!!CONGRATULATIONS YOU WON THE GAME!!!")
                
                
    if computers_score > users_score:
        print ("\n!!!COMPUTER WON THE GAME!!!")
                
            
     