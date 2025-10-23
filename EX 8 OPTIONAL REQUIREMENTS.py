#EX 8 SIMPLE SEARCH ADDITIONAL 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #initialize the list of names in variable "names"
search = input("Enter a name: ")  #asks the user to input a name and places inside variable 'search'

if search in names: #Searches for the given user input
    print(search, "was found in the list.") #if found, the code proceeds.  
else: 
    print(search, "was not found in the list.")

