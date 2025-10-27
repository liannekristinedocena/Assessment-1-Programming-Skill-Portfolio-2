#EX 3 ADVANCED REQUIRMENTS 
name = input("What is your name? : ") #asks the user to input their name 
hometown = input("Where do you live? : ") #asks the user to input their hometown 
age = input("How old are you? : " ) #asks the user to input their age 

info = {'name' : name, #adds the user input into a dictionary as key-value pairs
        'hometown' : hometown, 
        'age' : age} 

print(f"{info['name']}\n{info['hometown']}\n{info['age']}") 
#using f" or f-string automatically converts non-strings into strings, so when a user inputs an integer, f" converts it into a string instead of having to manually convert it ourselves. 
#input() reads entire lines, including spaces, so multi-words are accepted. 