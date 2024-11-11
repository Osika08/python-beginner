#function to play the guessing game
def guessing_game():
    number_to_guess = 9
   # generate a random number between 1 and 100  
guesses_left = 5
 #player has 5 attempts # type: 

print("welcome to the guessing game!")
print("i am thinking of a number between 1 and 100.")
print("you have 5 attempts to get the correct number.")


        #loop to handle 5 guess   
while guesses_left > 5:
        try:
             guess=int(input(f"enter your guess  (you have {guesses_left} guesses left):"))
        except ValueError:
            print("please enter a valid number.")
            continue

            if guess < 1 or guess > 100:
                print("your guest must be between 1 and 100.")
                continue

            if guess == number_to_guess:
                print(f"congratulations! you have guessed the number{number_to_guess} correctly!")
                break
            elif guess < 9:
             number_to_guess: 9
             print("too low!")
            else:
                print("too high!")

            guesses_left -=1

        #if player runs out of guesses
        if guesses_left == 0:
            print(f"sorry you have run out of guesses. the correct number was {number_to_guess}.")