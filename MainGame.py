from src.Live import load_game, welcome
from src.Utils import cls

if __name__ == '__main__':
    try:
        cls()
        print(welcome("Guy"))
        load_game()
    except KeyboardInterrupt as e:
        print("\nbye bye")
    except Exception as e:
        print(e)