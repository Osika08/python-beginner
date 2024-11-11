def greet_user(name):
 print(f"hello, {name}! welcome!")

    
def calculate_area(length,width):
 return length * width
area = calculate_area(5,10)
# print(area)


def is_even(number):
    return number % 2 == 0
# print(is_even(4))
# print(is_even(7))


def celsuis_to_fahrenheit(celsuis):
    return(celsuis * 9/5) + 32
fahrenheit = celsuis_to_fahrenheit(25)
# print(fahrenheit)


def find_largest(numbers):
    return max(numbers)
largest_number = find_largest([3,9,1,6,4])
# print(largest_number)


def print_table(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")


        