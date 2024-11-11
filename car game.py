def car_game():
    commands = {"start":"the car has started... ready to go!",
                "stop":"the car has stopped.",
                "help": ""
                  Available commands:
                -start: start the car_game
                -stop: stop the car
                -quit: exit the car
                ""}

car-started = False
car-stopped = True

print ("type 'help' to see available commands.")

while True:
     user_input = input(">").lower()

        if user_input == "start":
         if car_started:
            print("the car is already started.")
         else:
            car_started = True
            car_stopped = False

            print(commands["start"])
        elif user_input == "stop":
            if car_stopped:
               print("the car is already stopped.")
            else:
               car_stopped = True
               car_started = False

        print(commands["stop"])
     
        elif user_input == "help":
        print(commands["help"])
     
        elif user_input == "quit":
        print("exiting the game: Goodbye!")
        break
    else:
print("I do not understand that command. Type 'help' to see avauilable commands.")

#run the car game
car_game()
     


