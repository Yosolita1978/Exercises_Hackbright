import random

def choose_number():
    random_number = random.randint(1,100)
    return random_number

def ask_user():
    user_guess = int(raw_input("What is your guess?"))
    return user_guess
    
def play_game():
    number = choose_number()
    count = 0
    while True:
        try:
            guess = ask_user()
            if 0 < guess and guess < 101:
                count += 1
                if guess > number:
                    print "Your guess is too high, try again"
                elif guess < number:
                    print "Your guess is too low, try again"
                else:
                    print "Well done, You guessed the number in %i tries!" %(count)
                    break
            else:
                print "That is not within the range! FAIL!"
                break

        except ValueError:
            print "Gezz, Learn how to type a number!"
            break
    return count
        

def menu_game():
    prompt = """What do you want to do:

                1. Play
                2. Quit

             """
    user_choose = int(raw_input(prompt))
    return user_choose

def main():
    print "Welcome to the guessing game!"
    user_name = raw_input("What is your name?")
    best_score = float("inf")
    
    
    while True:
        user_choose = menu_game()
        if user_choose == 1:
            print "Hello %s! I am thinking of a number between 1 and 100." % (user_name)
            score = play_game()
            if score < best_score:
                best_score = score
                print "Congratulations, %s, you have the best score: %i tries" %(user_name, best_score)
                


        else:
            break
        

if __name__ == '__main__':
    main()




