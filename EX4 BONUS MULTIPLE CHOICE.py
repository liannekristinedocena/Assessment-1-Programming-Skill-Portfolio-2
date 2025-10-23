#PRIMITIVE QUIZ WITH BONUS (MULTIPLICE CHOICE)
print("Choices = Paris, Berlin, Athens, Budapest, Dublin, Rome, Moscow, Lisbon, Madrid, Stockholm") #prints all choices

Score = 0 #The 'Score' variable is used as a counter to track for the correct answers

answer1 = input("What is the capital of France? : ") #asks for user input and places it in the variable answer1 
if answer1.lower() == "paris" : #.lower() converts the user input into lowercase
    print("Correct!") #if condition is met, system prints out "Correct!"
    Score +=1 #Counter is incremented by 1
else: 
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 
    
    
answer2 = input("What is the capital of Ireland? : ") #asks for user input and places it in the variable answer2 
if answer2.lower() == "dublin" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises counter by 1 
else: 
    print("Wrong!")
    
    
answer3 = input("What is the capital of Sweden? : ")#asks for user input and places it in the variable answer3 
if answer3.lower() == "stockholm" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises counter by 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 
    
    
answer4 = input("What is the capital of Greece? : ")#asks for user input and places it in the variable answer4
if answer4.lower() == "athens" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises counter by 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 
    
     
answer5 = input("What is the capital of Germany? : ")#asks for user input and places it in the variable answer5
if answer5.lower() == "berlin" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises counter by 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 

    
answer6 = input("What is the capital of Russia? : ")#asks for user input and places it in the variable answer6
if answer6.lower() == "moscow" : #.lower() converts the user input into lowercase
    print("Correct!")
    Score+=1 #raises counter by 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 
    
      
answer7 = input("What is the capital of Italy? : ")#asks for user input and places it in the variable answer7
if answer7.lower() == "rome" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises counter by 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 
    
      
answer8 = input("What is the capital of Hungary? : ")#asks for user input and places it in the variable answer8
if answer8.lower() == "budapest" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises by counter 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 
    
    
answer9 = input("What is the capital of Portugal? : ")#asks for user input and places it in the variable answer9
if answer9.lower() == "lisbon" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises counter by 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 

 
answer10 = input("What is the capital of Spain? : ")#asks for user input and places it in the variable answer10 
if answer10.lower() == "spain" : #.lower() converts the user input into lowercase
    print("Correct!")#if condition is met, system prints out "Correct!"
    Score+=1 #raises counter by 1 
else:
    print("Wrong!") #if condition is not met, the string "Wrong!" is printed. 
    
print("You got", Score, "Out of ten questions correct!") #prints the total score the user has recieved with the use of the counter

    




