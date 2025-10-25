#EX5 ADVANCED REQUIREMENT : LEAP YEAR 
months = {1 : 31, 
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

if months2.isdigit():
    monthnumber = int(months2) 
    
    if 1<= monthnumber <=12 :
        if monthnumber == 2: #if the user input equals to 2, code proceeds to the 2nd user input
            leap = input("is the year a leap year? YES/NO : ") #asks user if the year is a leap year 
            if leap == "YES": #if input equals to "YES" the code proceeds with first condition
                print("Month 2 has 29 days.") #displays when leap == "YES
            else: 
                print("Month 2 has 28 days.") #displays when leap == "NO  
        else: 
            print(f"Month {monthnumber} has {months[monthnumber]} days.") 
    else: 
        print("That is not a valid month")
else: 
    print("That is not a number.")


