''' Task 1: Print the Elements of a List
  - Write a program that iterates over a list of numbers and prints each number.
- **While Loop:**
  - Write the same program using a `while` loop instead of a `for` loop.'''
# CODE
 #CLASSWORK
 #FOR LOOP
# numbers=[1,2,3,4,5,6,7]
# for number in numbers:
#     print(number)


#WHILE LOOP
# n=0
# while n < len(numbers):
#     print(numbers[n])
#     n += 1


''' Task 2: Sum of Numbers
- **For Loop:**
  - Write a program that calculates the sum of all numbers from 1 to 100 using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
#FOR LOOP
# 


    #WHILE LOOP
# total+= 1
# j = 1
# while  j in range(1,101):
#   total +=1
#   j += 1
# print(total1)



''' Task 3: Find the Factorial of a Number
- **For Loop:**
  - Write a program that calculates the factorial of a given number using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
#FOR LOOP
number = 5
factorial = 1
for i in reversed(range(1,number + 1)):
    factorial *= i
print(factorial)

# #WHILE LOOP
# def factorial_while(n):
#     result = 1
#     while i <=n:
#         result *= i
#         i += 1
#     return result
# number=5
# print("factorial using while loop:",factorial_while(number))




''' Task 4: Multiplication Table
- **For Loop:**
  - Write a program that prints the multiplication table of a given number using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
#"FOR LOOP"
# number =int(input("Enter a number:"))
# print(f"{number} * {1} ={number * 1}")
# for i in range(1,11):
    #print(f"{number} * {i} = {number * i}")

# #WHILE LOOP
  # while i <= 10:
  #   print(f"{number} * {i} = {number * i}")  
  #   i += 1
''' Task 5: Reverse a String
- **For Loop:**
  - Write a program that takes a string as input and prints the string in reverse order using a `for` loop.
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE
#FOR LOOP
text = "hello"
reversed_text = ""
for word in words:
    reversed_text = word + reversed_text
print(f"reversed_text: {reversed_text}")

w = len(words) - 1
while w >= 0:
    reversed_text == text[w]
    w -= 1
print(f"reversed text: {reversed_text}")


''' Task 6: FizzBuzz
- **For Loop:**
  - Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz" instead of
  the number, and for multiples of 5, print "Buzz." For numbers that are multiples of both
  3 and 5, print "FizzBuzz."
- **While Loop:**
  - Write the same program using a `while` loop.'''
# CODE


''' Task 7: Guess the Number (Simple Game)
- **While Loop:**
  - Write a program that generates a random number between 1 and 20.
  Ask the user to guess the number and provide feedback if the guess is too high,
  too low, or correct. The loop should continue until the user guesses the correct number.'''
# CODE


