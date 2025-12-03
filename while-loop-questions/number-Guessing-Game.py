"""number guessing game"""
import random

num = random.randint(1,10)
tries = 0

while True:
    guess = int(input("guess a number: "))

    if num == guess:
        tries += 1
        print(f"you are right, you guessed it in {tries} tries")
        break
    elif num > guess:
        tries +=1
        print("guess a little higher number")
    elif num < guess:
        tries += 1
        print("guess a little lower")  
    else:
        tries += 1
        print("you are wrong!")