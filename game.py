import random

print "Hello! Welcome to the guessing game!"
user_name = raw_input("What is your name?")
print "Hello %s! I am thinking of a number between 1 and 100." % (user_name)

def choose_number():
    random_number = random.randint(1,100)
    return random_number

def ask_user():
    user_guess = int(raw_input("What is your guess?"))
    return user_guess
    

number = choose_number()
count = 0
while True:
    guess = ask_user()
    try:
        if 0 < guess and guess < 101:
            count += 1
            if guess > number:
                print "Your guess is too high, try again"
            elif guess < number:
                print "Your guess is too low, try again"
            else:
                print "Well done %s, You guessed the number in %i tries!" % (user_name, count)
                play_again = raw_input("Would you like to play again? Y/N")
                if play_again == "N":
                    break

#                break
        else:
            print "That is not within the range! FAIL!"
            break
    except ValueError:
        print "Gezz, Learn how to type a number!"
        break



