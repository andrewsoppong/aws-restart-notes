# Exercise 1: Working with the if statement 

userReply = input("Do you need to ship a package? (Enter yes or no) ") #Getting information from the user

#Using the if statement to print the response 

if userReply == "yes":
    print("We can help you ship that package!") #Note the double equal sign is a comparative operator (==) 
else: # Exercise 2: Working with the else statement
    print("Please come back when you need to ship a package. Thank you.") #This handle sthe condition where the user doesn't want to ship a package

#Exercise 3: Working with the elig statetment 
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

