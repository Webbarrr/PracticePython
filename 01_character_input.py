#!/usr/bin/env python

# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

'''
Exercise 1 (and Solution)

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime
now = datetime.datetime.now()

class User:
    name = ""
    age = 0

class AgeCalculator:
    def WhenWillTheyTurnXYearsOld(self, age, x):
        return (now.year + x) - age


user = User()
age_calculator = AgeCalculator()

# get the name and age
user.name = input("Hey, what's your name?\n")
user.age = int(input("Okay {}, how old are you?\n".format(user.name.title())))

# tell them what year they will turn 100
message = "Okay {}, so if you're {} now then you should turn 100 in the year {}".format(user.name, user.age, age_calculator.WhenWillTheyTurnXYearsOld(user.age,100))
print(message)
print()

# extras
times_to_print = int(input("Give me a number:"))
print(message * times_to_print)
print()

message += "\n"
print(message * times_to_print)