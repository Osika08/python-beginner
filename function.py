#Defining a function
def greet():
    #Algorithm or instructions to Follow
    # word = "hello world"
     print("word")

#call the function
# greet()

def greeting():
    name=input("name: ")
    print(f"my name is {name}")

# greeting()

def calc():
     a =10 + 5
     b = a * 2
     c = 10 + b
     d = c - 5
     return d

# print(calc())

def color(object):
    return f"Favourite color: {object}"

# print(color(3456))

def add(n, x):
    return n + x

# print(add(10, 7))

def hi(name = "joy"):
    print(f"hello {name}")

hi()

def multi(length):
    for l in range(length):
        print(l)
    
# multi(5)

