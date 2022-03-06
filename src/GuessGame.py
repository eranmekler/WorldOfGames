import random

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    try:
        number = int(input("Please enter a number between 1 to " + str(difficulty) + ": "))
        while number < 1 or number > difficulty:
            number = int(input("Please enter a number between 1 to " + str(difficulty) + ": "))
        return number
    except ValueError as e:
        print("The error is... " + str(e.__class__) + "\nPlease start over!")



def compare_results(difficulty):
    number =  generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    answer = number == guess
    return answer



def play(difficulty):
    if compare_results(difficulty) == True:
        result = True
    else:
        result = False
    return result
