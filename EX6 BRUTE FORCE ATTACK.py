#EX 6

password = input("Enter the password : ") #asks the user to input the password
correct_pass = "12345" #defines the correct password as 12345

while password != correct_pass: #uses while loop to compare both passwords. WHILE user password is not equal to correct_pass, the code loops
    print("Try again!") #prints try again if passwords do not match
    password = input("Enter the password : ") #asks the user to input a password again until the correct one is inputted
else: 
    print("Welcome back!") #if password matches, welcome back! is printed. 
    

