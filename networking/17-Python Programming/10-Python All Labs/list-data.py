# Working with Lists, Tuples, and Dictionaries

#Exercise 1: Introducing the list data type

myFruitList = ["apple", "banana", "cherry"] #Creating a list, List uses the square bracket [], and elements are placed inside inverted commas, and seperated by comma.
print(myFruitList) #Printing list element to the terminal
print(type(myFruitList)) #Printing the Type of the myFruitList to the terminal

#Accessing a list by position 

print(myFruitList[0]) #This print 'apple' to the terminal 
print(myFruitList[1]) #This print 'banana' to the terminal 
print(myFruitList[2]) #This print 'cherry' to the terminal 

#Changing the Values in a list
myFruitList[2] = "orange"  #This changes 'cherry' to 'orange'
print(myFruitList) # Display the new modified list with 'orange'

#Exercise 2: Introducing the tuple data type 

myFinalAnswerTuple = ("apple", "banana", "pineapple") #Creating a Tuple. Tuple is created with round bracket with element placed inside inverted commas, and element seperated by comma
print(myFinalAnswerTuple) #This print the elements of your tuple to the terminal 
print(type(myFinalAnswerTuple)) #Print the type of the variable myFinalAnswerTuple, which is ofcourse a tuple

#Accessing a tuple by position 

print(myFinalAnswerTuple[0]) #Print the first element of the tuple i.e 'apple'
print(myFinalAnswerTuple[1]) #Print the second element of the tuple i.e 'banana'
print(myFinalAnswerTuple[2]) #Print the third element of the tuple i.e 'pineapple'

#Exercise 3: Introducing the dictionary data type

myFavoriteFruitDictionary = {
    "Akua" : "apple", 
    "Saanvi" : "banana",
    "Paulo" : "pineaple"
} # Creating a dictionary. Dictionary is created using a cury braces {}, and it have a key and value as an element in the dictionary

print(myFavoriteFruitDictionary)

#Accessing a dictionary by name 
print(myFavoriteFruitDictionary["Akua"]) #This will output 'apple'
print(myFavoriteFruitDictionary["Saanvi"]) #This will output 'banana'
print(myFavoriteFruitDictionary["Paulo"])  #This will output 'pineaple'

