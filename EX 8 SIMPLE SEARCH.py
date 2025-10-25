#EX 8 SIMPLE SEARCH

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #initialize the list of names in variable "names"
search = "Sam" #string "Sam" is placed in the variable 'search'

if search in names: #Searches for the string "Sam" in the list.
    print(search, "was found in the list.") #if found, the code proceeds.  
else: 
    print(search, "was not found in the list.") #displays if "Sam" is not found in the list.


