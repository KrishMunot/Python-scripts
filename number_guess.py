import random
import time
import sys

number = random.randint(1, 10)

def check(guessNum):
	if guessNum == number:
		print "Congrandulations! You have guessed the correct answer of %d!! You have won the game!!!" % (number)
		print("")
		sys.exit()
	elif guessNum > number:
		print "Sorry, your guess was too high :-/"
	elif guessNum < number: 
		print "Oops, your guess was too low :-("
	else:
		"It seems like your input wasn't a valid number"

def finalCheck(guessNum):
	if guessNum == number:
		print "Congrandulations!! You guessed the corerect answer of %d!! You have finnally won :-)" % (number)
	elif (guessNum > number) or (guessNum < number):
		print "Come on! I gave you 3 tries and you still couldn't guess my number  :-("
		time.sleep(.1)
		print "The correct answer was %d" % (number) 
	else:
		print "Man, you must have fucked someting up"
		
print "I'm thinking of a number between 1 and 10"
time.sleep(1)
print "..."

time.sleep(1)
guess = input("Can you guess my number?  > ")

check(guess)
print("")

guess = input("Guess agin  > ")

time.sleep(1)
print("")

check(guess)
print("")

print("You have guessed 2 times now.")
guess = input("Last try  > ")

time.sleep(1)
print("")

finalCheck(guess)

print("")
sys.exit()
