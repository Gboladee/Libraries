import random
print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")
attempt = 0
while True:
    pickNum = int(input("Guess the number!:  "))
    correctAns = random.randint(1, 1000000)
    if pickNum < 0:
        print("That is a negative number, Goodbye!")
        exit()
    if pickNum > correctAns :
        print("Too High, Try Again!")
        attempt+= 1
    elif pickNum < correctAns :
        print("Too low, Try again!!")
        attempt += 1
        continue
    elif pickNum == correctAns :
        print("Correct, You are a star !!!!!")
        attempt += 1
        break
    else:
        print("That does not count")
print("You guessed this correctly after", attempt, "attempt(s)")