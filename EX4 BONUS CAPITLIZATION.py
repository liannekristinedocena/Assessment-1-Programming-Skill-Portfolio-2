#PRIMITIVE QUIZ WITH BONUS (CAPTILIZATION)

answer = input("What is the capital of france? : ") #takes user input in the variable 'answer'

if answer.lower() == "paris" : 
    
    '''.lower in python converts the user input into all lowercase letters, so PARIS 
= paris, PaRIS = paris, pARIs = paris, etc. So the answer is considered correct despite 
capitilization'''

    print("Your answer is correct! Congratulations.") #Prints if the answer is == paris 
else: 
    print("Your answer is wrong!") #prints if the answer given by user is incorrect 


