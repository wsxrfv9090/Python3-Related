#!/bin/python3

#print string
print("Strings and stuff: ")
print('Hello world')
print("""Hello, this is a 
multi-line string""")
print("This is a " + "split string")

print('\n') #new line
def new_line(): #new line function
	print('\n')

#math
print("math time!: ")
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiplication
print(50 / 50) #division
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) #number without leftovers (without float)

new_line()

#Variables & Methods
print("Fun with Variables and Methods: ")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title

name = "Davy Yu"
age = 20 #interger
gpa = 2.0 #float

print(int(age))
print(int(29.9)) #does not round
print("My name is " + name + ", and I'm " + str(age) + " years old" + ". My gpa is " + str(gpa))

new_line()

age += 1
print(age)

birthday = 1
age += birthday
print(age)

new_line()

#Functions
print("Function time!: ")
def who_am_i():
	name1 = "Davy Yu"
	age1 = 20
	gpa1 = 2.2
	print("My name is " + name1 + ", and I'm " + str(age1) + " years old" + ". My gpa is " + str(gpa1))

who_am_i()

#Adding in parameters
def add_one_handred(num):
	print(num + 100)

add_one_handred(100)

#Add in multiple parameters
def add(x,y):
	print(x + y)
	
add(7,7)
add(100,100)

#Using return
def multiply(x,y):
	return x * y
	
print(multiply(7,7))

def square_root(x):
	return x ** .5

print(square_root(4))

new_line()

#Boolean expressions (Truth or False)
print("Boolean expressions")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and1 = (7 > 5) and (5 < 7)
test_and2 = (7 > 5) and (8 < 5)
test_or1 = (7 > 5) or (5 < 7)
test_or2 = (7 > 5) or (8 < 5)
test_not = not True

print(test_and1, test_and2, test_or1, test_or2, test_not)

new_line()

#Conditional Statements
print("Conditional Statements: ")
def soda(money):
	if money >= 2:
		return "You got yourself a soda!"
	else:
		return "No soda for you today!"
		
print(soda(3))
print(soda(1))

new_line()

def alcohol(age, money):
	if (age >= 21) and (money >= 5):
		return "We've got some Choronas!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money"
	elif (age < 21) and (money > 5):
		return "Nice try kiddo"
	elif (age < 21) and (money < 5):
		return "You're too poor and too young, that's miserable"

print(alcohol(22,7))
print(alcohol(22,2))
print(alcohol(10,8))
print(alcohol(3,3))

new_line()

#Lists
print("Lists have brackets: ")
movies = ["When Harry Met Sally", "The Hungover", "The Perks Of Being A Wallflower", "The Exorcist"]

print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("JAWS")
print(movies)

movies.pop()
print(movies)

movies.pop(1)
print(movies)

movies = ["When Harry Met Sally", "The Hungover", "The Perks Of Being A Wallflower", "The Exorcist"]
person = ["Heath", "Jack", "Leah", "Jeff"]
conbined = zip(movies, person)
print(list(conbined))

movies = ["When Harry Met Sally", "The Hungover", "The Perks Of Being A Wallflower", "The Exorcist"]
person = ["Heath", "Jack", "Leah"]
conbined = zip(movies, person)
print(list(conbined))
new_line()

#Tuples
print("Tuples have parentheses and cannot change")
grades = ("A", "B", "C", "D", "F")
print(grades[1]) #You can't use append or pop

#Looping
print("For loop --- start to finish of iterate: ")
vegetables = ["Cucumber", "Spinach", "Cabbage"]
for x in vegetables:
	print(x)
	
print("While loop --- Execute while its true")
i = 1
while i < 10:
	print(i)
	i += 1;














































