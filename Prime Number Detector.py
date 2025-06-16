def detector(number):
    if number <= 1:
        return False
    
    for i in range (2, number):
        if number % i ==0:
            return False
    else:
        return True

while True:
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
