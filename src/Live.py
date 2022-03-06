def welcome(name):
    return str("Hello " + name + " and welcome to the World of Games (WoG)." " \nHere you can find many cool games to play.")

def load_game():
    print(str("Please choose a game to play:\n\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n\t2. Guess Game - guess a number and see if you chose like the computer\n\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS "))
    try:
        game = int(input("Enter the number here: "))
        if game < 1 or game > 3:
            print("Please enter a number between 1 - 3")
        else:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty < 1 or difficulty > 5:
                print("Please enter a number between 1 - 5")
    except ValueError as e:
        print("The error is... " + str(e.__class__) + "\nPlease enter a number.")

    if game == 1:
        from src.MemoryGame import play
        if play(difficulty) == True:
            from src.Score import add_score
            add_score(difficulty)
            print('\nYou won! ')
        else:
            print('\nYou lose! Try again! ')
    elif game == 2:
        from src.GuessGame import play
        if play(difficulty) == True:
            from src.Score import add_score
            add_score(difficulty)
            print('\nYou won! ')
        else:
            print('\nYou lose! Try again! ')
    elif game == 3:
        from src.CurrencyRouletteGame import play
        if play(difficulty) == True:
            from src.Score import add_score
            add_score(difficulty)
            print('\nYou won! ')
        else:
            print('\nYou lose! Try again! ')

