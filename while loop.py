while user_trial < number_of_trial:
    response = int(input("guess the number on my mind!"))
    if response == secret_number:
        print("correct you guessed right!!!")
        break
    else:
        print("No you are WRONG!!!!!!!!")
        user_trial += 1

    if user_trial == number_of_trial:
        print("sorry you have run out of trials!")
        reply =str(input("type quit to end game"))
        if reply == "quit":
            break
