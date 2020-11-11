#Author: Alan  

#Date 11/11/2020 

#Version: 1.0 

# 

#Guess the randomn number game 

#One player vs. the computer 

 
 

import random 

minGuess= 1 

maxGuess= 6 

 
 

#Ask the user for their their name and their guess  

name = input("What is your name? ") 
print("Hi + name!") 
print("Enter a number between: "+ minGuess + "and" + maxGuess) 
guess = int(input("What is your guess? ")) 
 

#Generate a random number and tell the user if they won or lost 
secretNumber = random.randint(minGuess, maxGuess) 
if (guess != secretNumber 
  print("Congratulation, you got it right!") 
else:  
  print("You lose - the number was secretNumber") 
 

print("Thank you for playing Guess the Number.") 

#??? lines completed but still has all the other errors 

 