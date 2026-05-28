#Exercise 1: Working with a while loop

#Importing modules 
import random 

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#This statment generate a random number between 1 and 10
number = random.randint(1,10)

#Track whether the user guessed your number right 
isGuessRight = False #False value is initially assigned to the variable isGuessRight

#Using a while loop to handle the logic of the guess game application
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

"""
This is a multi-line comment
A pseudocode is a generic language used to describe an algorithm. 
1. if the user has not guessed the correct answer, enter the loop
2. Ask the user for a guess. 
3. Is the guess the correct number? 
4. If it is a correct guess, tell the user it was the correct guess and exit the loop. 
5. If the guess is wrong, tell the user it was the wrong guess and continue looping
"""