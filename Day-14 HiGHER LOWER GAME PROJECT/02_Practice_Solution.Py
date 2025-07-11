# HINTS:
        # Display art

        # Generate a random account from the game data.

        # Format account data into printable format.

        # Ask user for a guess.

        # Check if user is correct.
        ## Get follower count.
        ## If Statement

        # Feedback.

        # Score Keeping.

        # Make game repeatable.

        # Make B become the next A.

        # Clear screen between rounds.

from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got"""
    if a_followers > b_followers:
        return guess == "a"
    if a_followers < b_followers:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more follower? Type 'A' or 'B'.").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    if is_correct:
        score += 1
        print(f"You're right! Current Score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score {score}.")