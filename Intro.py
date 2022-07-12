import random
print("Number guessing game")
number = random.randint(1,10)
chances = 0
print("Guess a number between(1 and 9):")

while chances <5 :
    guess = int(input("Entre your guess:-"))

    if guess == number:
        print("Congrats You Won")
        
        break 
    elif guess < number :
        print("Your guess was just too low:Guess a number higher than that", guess)

    else:
        print("Your guess was too higher:Guess a number lower than that", guess)

        chances += 1

if not chances <5 :
    print("You Lose the number is", number)

