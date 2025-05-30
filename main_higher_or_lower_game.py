
#Display art
from art import logo, vs
from game_data import data
import random
print(logo)


score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    def format_data(account):
        # Format the account data and returns printable format
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    def check_answer (user_guess, a_followers, b_followers):
        #""""Take the users guess and the follower counts of a and b and returns if they got it right""""
       # Returns True or False
        if a_followers > b_followers:
            return user_guess == "a"
        else:
            return user_guess =="b"



    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print (f"Compare A: {format_data(account_a)}.")
    print (vs)
    print (f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? 'A' or 'B': ").lower()
    #clear the screen
    print("\n"*20)
    print (logo)

    # check if user is correct
    ## get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    ## use if statement to check if user is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score +=1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Your score is: {score}")
        game_should_continue = False




    # give user feedback on their guess

    # track score

    # make the game repeatable

    # making accounts at position B become the next account at position A



