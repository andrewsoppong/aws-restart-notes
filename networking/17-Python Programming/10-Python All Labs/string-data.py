#Workign with the String Data Type 

#Creating myString variable 

myString = "This is a string. "
print(myString) #This print to the terminal 
print(type(myString)) #This prints the data type of the variable myString
print(myString + " is of the data type " + str(type(myString)))

#Working with String Concatenation 

firstString = "water" #Assigning 'water' to the firstString variable
secondString = "fall" #Assigning 'fall' to the secondString variable
thirdString = firstString + secondString #Concatenating using '+' with firstString and secondString
print(thirdString) #Printing the thirdString to the terminal 

# Working with input Strings 

name = input("What is your name? ") #Taking keyboard input from the user i.e user name
print(name) #Printing what the user typed on the keyboard

# Exercise 4: Formatting output strings 

color = input("What is your favorite color? ") #Favorite color keyboard input from the user
animal = input("What is your favorite animal? ") #Favorite animal keyboard input from the user 

print("{}, you like a {} {}!".format(name, color,animal)) #Using string formating to print to the terminal 


