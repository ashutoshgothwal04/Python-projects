import random

def Guess():
 
    randomNumber = random.randint(1, 50)  # Add minimum and maximum values
    guesses = 0
    user = -1   
    while(user!=randomNumber):
         user = int(input("Choose your number 1-50 : "))
         if user > randomNumber:
             print("Lower no please.")

         elif user < randomNumber:
          print("Higher no please.")
          guesses += 1

         else:  # Remove the redundant else clause
             print(f"Congratulation! you choose right no {randomNumber} in {guesses} guesses")
             guesses += 1

Guess()