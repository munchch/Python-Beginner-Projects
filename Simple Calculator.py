
        
while True: #Used while to make algorithm work in a loop
    welcoming= input("\nWelcome! Please text c to continue or q to quit:") 
    if welcoming.lower() == "q": #Used .lower to prevent issue deriving from uppercase q input
        break
    elif welcoming.lower() != "c":
        print("Invalid input please enter either c or q!")
        continue
  
    try:
        
        number1= int(input("Please enter the first number: "))
        number2= int(input("Please enter the second number: "))
        operation= input("Please enter the math operation (+, -, *, /):")
        
        if operation not in ["+", "-", "*", "/"]: #Controlled operation inputs
            print("Invalid operation! Please use +, -, *, or /.")
            continue
            
            
        if operation == "+":
            print(str((number1+number2))+ " is the result")
        
        elif operation == "-":
            print(str((number1-number2))+ " is the result")
            
        elif operation == "/":
            if number2== 0: #Prevented the peculiar situation zero as a denominator 
                print("Zero cannot be a denominator")
            else:
                print(str((number1/number2))+ " is the result")   
            
            
        elif operation == "*":
            print(str((number1*number2))+ " is the result")
            
    except: 
        print("Please enter viable values")
    

    
    
        
