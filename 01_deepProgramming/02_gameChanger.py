print("Welcome!")
g =  input("Guess a number: ")
guess = int(g)
if guess == 5:
        print("You win!")
else:
        if guess > 5:
                print("Guess is too high")
        else:
                print("Guess is too low")
        print("Not yet!")
print("Game over!")
