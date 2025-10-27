#EX 3 ADVANCED REQUIRMENTS 
name = input("What is your name? : ") #asks the user to input their name 
hometown = input("Where do you live? : ") #asks the user to input their hometown 
age = input("How old are you? : " ) #asks the user to input their age 

while True: #while loop enables the code to repeat until user inputs a valid age
        age = input("How old are you? : " ) #asks user to input their age and places it inside the "age" variable
        if age.isdigit(): #checks if all characters are digits 
                age2 = int(age) #uses the int function to convert variable age into an integer and declares it as variable "age2" 
                break #breaks or exits the loop
        else:
                print("Please enter a number! : " ) #asks the user to enter a number 
        

info = {'name' : name, #stores the user input into a dictionary as key-value pairs
        'hometown' : hometown, 
        'age' : age} 

print(f"{info['name']}\n{info['hometown']}\n{info['age']}") 
#using f" or f-string automatically converts non-strings into strings, so when a user inputs an integer, f" converts it into a string instead of having to manually convert it ourselves. 

#input() reads entire lines, including spaces, so multi-words are accepted. 
