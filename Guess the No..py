'''import random

lower = int(input("Enter Lower no."))
upper = int(input("Enter Upper No."))
x = random.randint(lower,upper)
guess = int(input("Guess the number"))  

if guess<lower or guess>upper :
    print("sahi number daal bhai")

while guess != x:
    guess = input("Guess again:")      
    if guess == "x":
        print('Congo You Won')
        break
    else :
        print('Try Again')'''
import random             
def Guesses():
    lower = int(input("Enter Lower Number."))
    upper = int(input("Enter Upper Number"))              
    num = random.randint(lower,upper)
    guess = None
    
    while guess != num:
        guess = input("guess a number between "+str(lower)+' and '+str(upper)+' numbers')
        guess = int(guess)   
        if guess == num:
            print("congratulations! you won!")
            break
        else:
            print("nope, sorry. try again!")
            
Guesses()            