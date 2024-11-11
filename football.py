#the football game prediction
random = list(range(7))
for x in random[0:3]:
    for y in random:
        result = (f"{x} - {y}")

trial = 3
count = 0


while count <= trial:
    user_response = input("enter your prediction below\n ")
    if user_response == result:
        print("correct")
        break
    else:
        print("wrong!!!")
        count += 1

        if count == trial:
            print("sorry, you have run out of trials!")
            break