import random
import requests

def get_money_interval(difficulty):
    r = requests.get("http://api.currencylayer.com/live?access_key=1a10e765ea63f7c7c6f2c4cd08c79579&currencies=ILS&format=1")
    r_dict = r.json()
    current = r_dict['quotes']['USDILS']
    amount = random.randint(1, 100)
    total_value = current + amount

    # For given difficulty d, and total value of money the interval will be: (t - (5 - d), t + (5 - d))
    result = (total_value - (5 - difficulty), total_value + (5 - difficulty))
    return (amount, result)


def get_guess_from_user(amount):
    try:
        guess = float(input("pleas enter a guess of value of " + str(amount) + " USD in NIS: "))
    except ValueError as e :
        print("The error is... " + str(e.__class__) + "\nPlease enter a number.")
    return guess

def play(difficulty):
    vars = get_money_interval(difficulty)
    amount = vars[0]
    result = vars[1]
    guess = get_guess_from_user(amount)

    if result[0] < guess > result[1]:
        final = True
    else:
        final = False
    return final








