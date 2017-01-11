# your code goes here
RESTAURANT_RATINGS_ORIGINAL = {}

def build_restaurant_ratings(filename):
    rating_file = open(filename)

    for line in rating_file:
        line = line.rstrip()
        restaurant, rating = line.split(':')

        RESTAURANT_RATINGS_ORIGINAL[restaurant] = rating

    return RESTAURANT_RATINGS_ORIGINAL

def print_restaurant_rating(dictionary):

    for restaurant, rating in sorted(dictionary.items()):
        # dictionary[restaurant] = dictionary.get(rating)
        print "{} is rated at {}.".format(restaurant, rating)

def add_user_rating():
    user_restaurant = raw_input("What restaurant would you like to rate: ")
    user_rating = -1
    while user_rating not in range(0, 6):
        user_rating = int(raw_input("What would you like to rate the restaurant (0-5): "))

    RESTAURANT_RATINGS_ORIGINAL[user_restaurant] = user_rating


user_choose = 0
build_restaurant_ratings('scores.txt')
while user_choose != 3:
    user_choose = int(raw_input("What do you want to do: 1 - See rating 2 - Add a rating 3 - Quit: "))
    if user_choose == 1:
        print_restaurant_rating(RESTAURANT_RATINGS_ORIGINAL)
    elif user_choose == 2:
        add_user_rating()
    else:
        break