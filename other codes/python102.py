#!/bin/python3

#Importing
print("Importing is important: ")

import sys #System functions and parameters
from datetime import datetime #its like headers in C
print(datetime.now())

from datetime import datetime as dt #Importing with an alias
print(dt.now())

def new_line():
	print("\n")
	
new_line()

#Advanced String
print("Advanced strings: ")
my_name = "Davy"
print(my_name[0]) #first initial
print(my_name[-1]) #last initial

sentence = "This is a sentence."

print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word

print(sentence.split()) #split sentence by delimiter space (default)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said, 'Give me all your money'"
print(quoteception)

quoteception = "I said, \"Give me all your money\""
print(quoteception)

quoteception = """I said, "Give me all your money\""""
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter in word)
print(letter in word.lower()) #Improved --case-insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())) #true and not false, hence the outcome is True

too_much_space = "           hello          "
print(too_much_space.strip())

full_name = "davy Yu"
print(full_name.replace("davy", "Davy"))
print(full_name.find("Yu"))

#PlaceHolder
movie = "The Hungover"
print("My favorite movie is {}.".format(movie))

def favorite_book(title, author):
	fav = "My favorite book is \"{}\", which is written by {}.".format(title,author)
	return fav

print(favorite_book("The Great Gatsby", "F. Scott Fitzgerald"))

new_line()

#Dictionaries
print("Dictionaries are keys and values")
#lists []
#tuples ()
#dictionaries {}

drinks = {"White Russians": 7, "Old Fashion": 10, "Lemon drop": 8, "Buttery Nipple": 6} #drink is key, price is value
print(drinks)

employees = {'Finance': ["Bob", "Linda", "TIna"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
employees['legal'] = ["MR.Froud"] #add new key: value pair
print(employees)
employees.update({"Sales": ["Andie", "Ollie"]}) 
print(employees)

drinks['White Russians'] = 8
print(drinks)
print(drinks.get("White Russians"))
print(drinks.get("Martini"))
print(drinks["White Russians"])

new_line()

movies = ["Harry Potter", "Transformers", "The Avengers", "New Mutants"]
person = ["Davy", "Yu", "yxy", "Ouyang Yutong"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}
print(movie_dictionary)












































