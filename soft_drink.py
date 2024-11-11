import sys
total_cost = int(input("Total: "))

#ask for payment
print("how are you making payment")
print("1.cash payment\n2. bank payment")

#prompt for their tye of payment
payment = input("payment:")

# If statement
# If cash payment
if payment=='cash' or payment=='1':
    #ask them how much they have
    amount = int(input("how much do you have?")) 

if amount< total_cost:
    print("insufficient balance")
    sys.exit()
    #Deduct the total cost from the cash amount  
    change= amount - total_cost
    #print their balance e.g your balance is N600
    print(f"your remaining balance is {change}")
 #Elif bank payment
elif payment=='bank' or payment=='2':
    #tell them you have deducted their money. e.g we have deducted N600 from your account
    print(f"{total_cost} has been deducted from your account")




