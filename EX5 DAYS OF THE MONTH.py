#EX 5 DAYS OF THE MONTH 

months = {1 : 31, #puts the days of the months into a dictionary with the month being the key and the days being the value 
          2 : 28, 
          3 : 31, 
          4 : 30, 
          5 : 31, 
          6 : 30,
          7 : 31, 
          8 : 31, 
          9 : 30, 
          10 : 31, 
          11 : 30, 
          12 : 31}

months2 = input("Input the month number! : ") #asks the user to input a number from the dictionary (1-12)

if months2.isdigit(): #using .isdigits(): helps check if all characters in a string are classified as integers / digits 
    monthnumber = int(months2) #int converts the string input into an integer and places it in a new variable named 'monthnumber' 
    if 1<= monthnumber <=12 : #checks whether or not the user input is within the range 1-12 
        print(f"Month {monthnumber} has {months[monthnumber]} days.") #prints the key-value pair from the dictionary 
    else: 
        print("That is not a valid month") #displays when the numbers are outside the range
else: 
    print("That is not a number.") #displays when the value is a string and not an integer 



