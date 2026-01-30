import sys #system functions and parameters
from datetime import datetime as dt #using an alias


#importing is important 
print(sys.version)


# here wo go, 2nd time lucky
print("Hello, World")
print('Hello, world - again')
print("""now we are 
going to write
across 3 lines""") #what what whaaaat
print("this is a "+"string") #concatenation
print('\n')
print("test the new line")
#math
print(50 + 50)
print(50 - 50)
print(50 / 50)
print(50 * 50)
print(50 + 50 - 50 * 50 / 50) #Parentheses, Exponents, Multiplication and Division (left to right), and Addition and Subtraction (left to right). 
print(50 ** 2) #exponents
print(50 / 6) #division with a remainder
print(50 % 6) #medulo - takes what is left over (50 div and what is left, is 2)
print(50 // 6) #no remainder at all

print('\n')
#variables and methods
#variable is an object we can store into 
age = 35 #interger object - age is variable and number is the integer
name = "Allan" #string
gpa = 3.8 #float
print(int(age))
print(int(35.1))
print(int(35.9)) # will it round? no - ignores the float

quote = "It is what it is"
print(quote)

# methods - function that is defined within a class mini program
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #count all characters

print("My name is " + name)
print("My name is "+name+" and I am "+str(age)+" years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
#user input
# x = float(input("Give me a number: "))
# y = input("Give me a another number: ")
# print(x + float(y))

print('\n')

# Functions - Reusable block of code (like a program)

#def who_am_i(name,age):
    #name = "Allan" #local var - only true to func right here
    #age = 40
    #print("My name is {name} and I am {age} years old")

#who_am_i("Allan", 40)

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

result1 = multiply(7,7)
result2 = multiply(8,8)
print(result1 - result2)

def square_root(x):
    print(x ** .5)

square_root(81) #build our own math functons

def nl():
    print('\n')

nl()

#Boolean Expressions (True or False)
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

#reltional & boolean operators

greater_than = 7 > 5 
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
equals = 7 == 7
not_equals = 7 != 8

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #true
test_not = not True #False

nl()
#Conditional Statements if/else

def drink(money):
    if money >= 2:
        return "You've got yourself a drink"
    else: 
        return "No drink for you!"
print(drink(3))
print(drink(1))

nl()

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "You've got yourself a drink"
    elif (age >= 21) and (money < 5):
        return "Go get money cheapskate"
    elif (age < 21) and (money >=5):
        return "Nice Try Buddy!"
    else:
        return "You are too young and too poor womp womp."
    
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()

#let's see if this updates now
#loops Jeremy

#For Loops - Start to finish of an iterate
vegetables = ["Cucumber", "Spinach", "Cabbage"]
for veggies in vegetables:
    print(veggies)

for i in range(5):
    print(i)

word = "Python"
for letter in word:
    print(letter)

#While Loop - as long as true
i = 1

while i < 10:
    print(i)
    i += 1

#password = ""

#while password != "spaghetti":
   # password = input("Enter the secret password: ")

#print("Access Granted")

# Building a Calculator
nl()
#Lists - Comprises of items in [] brackets 

movies = ["Lord of the Rings", "Talledega Nights", "Step Brothers", "Your Highness"]

print(movies[1]) #0 = 1, 1 = 2, 2 = 3 & 3 = 4
print(movies[0:2]) #returns the first number given up to before the last
print(movies[1:4]) #returns movies 1 - 3
print(movies[:2]) #everything before 2
print(movies[-1]) #last one

print(len(movies)) #counts items in list
movies.append("Jaws") #adds item to the end of our list
print(movies)

movies.insert(2, "Jumanji")
print(movies)

movies.pop() #removes last item
print(movies)

movies.pop(0) #removes first item
print(movies)

amber_movies = ["one", "two"]
our_favourite_movies = movies + amber_movies
print(our_favourite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 88]]
bobs_grades = grades[0][1]
print(bobs_grades)
grades[0][1] = 83
print(grades)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])

#Tuples - Immutable - Can't be changed
#
Coordinates = (40.7128, 74.0060) #New York
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
student = ("John Doe", 5564865, "Computer Science")

print(student[1])

nl()

#Dictionaries - Key/value pairs {}

drinks = {"White Russian": 8, "Old Fashioned": 12, "Lemon Drop": 5}#drink is key/ price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Jean", "Louise", "Teddy"], "HR": ["Jimmy Jnr", "Mort"]}
print(employees)
employees['Legal'] = ["Mr. Frond"] #key value pair added
print(employees)

employees.update({"Sales": ["Andy", "Olly"]}) #also adds new vp
print(employees)

drinks['White Russian'] = 9
print(drinks)

print(drinks.get("White Russian"))

#strings again - but advanced

nl()

my_name = "Allan"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence. "
print(sentence[:4])

print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = '-'.join(sentence_split)
print(sentence_join) #removes the spaces

quote = "Bingo Said, 'To be or not to be - that is a question'"
quote = "Bingo said, \"To be or not to be - that is a question\"" 
print(quote)

too_much_space = "                          Hello   "
print(too_much_space.strip())

#booleans 
print("A" in "Apple") #return True - case sensitive
print("a" in "Apple") #return False - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

#user_input = input("Enter yes or no: ")
#if user_input.lower().strip() == "yes":
#    print("You Agree! ")
#else: 
#    print("You disagree!")

movie = "The Hangover"
print("My Favourite movie is {}.".format(movie))
print("My Favourite movie is %s." %movie)
print(f"my favourite move is {movie}. ")

print(sys.version)
print(dt.now())