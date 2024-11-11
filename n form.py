response = str(input("welcome to platform school,what would you like to do?\n1. enroll \n2. class \n3. enquiry\n")).lower()

if response == "1" or response == "enroll":
    first_name = str(input("enter your first name\n")).upper()
    last_name = str(input("enter your last name\n")).upper()
    email = str(input("enter your email\n")).upper()