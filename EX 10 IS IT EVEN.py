#EX 10 IS IT EVEN? 

def even_odd(number): #defines the function even_odd that will determine whether the number is even or odd.
    if number % 2 == 0: #checks if the number, when divided by 2, will equal to 0
        return f"{number} is even." #returns a message saying that the given number is even
    else: 
        return f"{number} is odd." #if not divisible, the code will return a message saying that the number is odd
        
def main(): #defines the main function 
    number_2 = int(input("Please enter a number: ")) #asks the user to input a number that will be placed in variable number_2
    
    result = even_odd(number_2) #calls the even_odd function with user input in a variable called result 
    print(result) #prints the result 
    
if __name__ == "__main__": #enables the program to run properly 
    main() #calls onto the main function to execute the program 



