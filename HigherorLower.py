from game_data import data
from art import *
import random
import os

# Get a dictionary of all the necessary information
follower_count = {}
desc = {}
country = {}

for profile in data:
    follower_count[profile['name']] = profile['follower_count']
    desc[profile['name']] = profile['description']
    country[profile['name']] = profile['country']

profile_names = [name['name'] for name in data]

# Lists for holding information
first_profile = []
second_profile = []
first_compared_follower_count = []
second_compared_follower_count = []

def main():
    global first_compared_follower_count, second_compared_follower_count
    score = 0
    # Establish a loop where it doesn't end until user gets an incorrect answer
    game_loop = True
    # To start pick two random names to compare and get their follower counts
    while True:
        try:
            first_profile = pick_a_profile(first_compared_follower_count)
            second_profile = pick_a_profile(second_compared_follower_count)
            if first_profile == second_profile:
                raise ValueError
        except ValueError:
            pass
        else:
            break
    while game_loop:
        print(logo)
        print('Who has more followers?')
        print(first_profile)
        print(vs)
        print(second_profile)
        while True:
            try:
                guess = input("Type 'A' for the first option or 'B' for the second option.\n").upper()
                if guess not in ('A','B'):
                    raise ValueError
            except ValueError:
                print("Type 'A' or 'B'.")
            else:
                break
        if guess == more_followers(first_compared_follower_count, second_compared_follower_count):
            score += 1
            pass
        else:
            print(f'You had a score of {score}. Game over.')
            break
        
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            try:
                first_profile = second_profile
                name = first_profile.split(',')[0]
                second_profile = pick_a_profile(second_compared_follower_count)
                first_compared_follower_count = follower_count[name]
                if first_profile == second_profile:
                    raise ValueError
            except ValueError:
                pass
            else:
                break




#create a function that picks a profile and returns a description of the profile
# And adds 
def pick_a_profile(var):
    global first_compared_follower_count, second_compared_follower_count
    random_name  = random.choice(profile_names)
    random_follower_count, random_desc, random_country = follower_count[random_name], desc[random_name], country[random_name]
    if var == first_compared_follower_count:
        first_compared_follower_count = random_follower_count
    elif var == second_compared_follower_count:
        second_compared_follower_count = random_follower_count
    return f"{random_name}, a {random_desc}, from {random_country}"


# Create a function that finds the more followed of the two being compared
def more_followers(A, B):
    if A > B:
        return "A"
    else:
        return "B"


if __name__ == "__main__":
    main()