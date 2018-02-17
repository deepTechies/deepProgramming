from random import randint
secret = randint(1, 10)

print("Welcome!")

guess = 0
while (guess != secret):
        g =  input("Guess a number: ")
        guess = int(g)      
        if guess == secret:
                print("You win!")
        else:
                if guess > secret:
                        print("Guess is too high")
                else:
                        print("Guess is too low")
                print("Not yet!")
print("Game over!") 
