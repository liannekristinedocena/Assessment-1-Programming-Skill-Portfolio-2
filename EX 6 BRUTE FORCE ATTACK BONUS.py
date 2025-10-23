#EX 6 BONUS
correct_pass = "12345"

attempt1 = 5 #max number of attempts 
attempts = 0 #sets the counter at 0 

while attempts < attempt1 : #uses while loop to continue the code until the max number of attempts is reached
    password = input("Enter the password : ") #asks user to input the password
    
    if password == correct_pass : #checks if the entered password is equals to the correct password
        print("Welcome in!") #if condition is met, the message is displayed and exits the loop
        break
    else: 
        attempts +=1 #if incorrect, the attempts is increased by 1 
    remaining_attempts = attempt1 - attempts #calculates how many attempts are left and places it inside the remaining_attempt variable
    
    if remaining_attempts > 0: #if the remaining attempt is greater than 0, the condition is true 
        print("You have", remaining_attempts, " attempts left.") #lets the user know how many attempts they have left. 
    else: 
        print("The authorities have been alerted.") #if no attempts are left, this message is displayed. 
    
        