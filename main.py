from datas import data
import random


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return print(f"{name} as {description} from {country}")


def answer_check(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    account_a = random.choice(data)
    account_b = random.choice(data)
    continue_game = True
    score = 0

    while continue_game:
        account_a == account_b
        account_b = random.choice(data)

        while account_a == account_b:
               account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(f"Compare B: {format_data(account_b)}")
        guess = input("Does A has more followers or B?").lower()

        is_true = answer_check(guess, account_a["follower_count"], account_b["follower_count"])

        if is_true:
            score += 1
            print(f"Correct! Score: {score}.")
        else:
            continue_game = False
            print(f"Wrong! Score: {score}")


game()
