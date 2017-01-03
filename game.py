import random

#greet player
#get player name
#choose random number between 1 and 100
#while True:
#    get guess
#    if guess is incorrect:
#        give hint
#        increase number of guesses
#    else:
#        congratulate player# Put your code here

print "Hello! Welcome to the guessing game!"
user_name = raw_input("What is your name?")
print "Hello %s! I am thinking of a number between 1 and 100." % (user_name)
random_number = random.randint(0,101)
print random_number


count = 0

while True:
    user_guess = int(raw_input("What is your guess?"))
    count += 1
    if user_guess > random_number:
        print "Your guess is too high, try again"
    elif user_guess < random_number:
        print "Your guess is too low, try again"
    else:
        print "Well done %s, You guessed the number in %i tries!" % (user_name, count)
        break


