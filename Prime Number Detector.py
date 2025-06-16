def detector(number):
    if number <= 1:  # Excluded numbers smaller than 1 (including one) as not prime number because they are not
        return False
    
    for i in range (2, number): # An algorithm divides every number from 2 to given number to the given number and testing if there is a residual
        if number % i ==0:
            return False
    else:
        return True

while True: # Used while so that algorithm could be in a loop
    number = (input("\nEnter the number you want to check or q to quit:"))
    if number.lower() == "q":
        break
   
    try:
        number = int(number)
        if detector(number):
            print(str(number)+" is a prime number")
        else:
            print(str(number)+" is not a prime number")
            
    except:
        print("Invalid input! Please enter an integer or 'q' to quit.")
