import random
import os
from time import sleep
from src.Utils import cls


def generate_sequence(difficulty):
    sequence = random.sample(range(101), difficulty)
    print(sequence)
    sleep(0.7)
    cls()
    return sequence

def get_list_from_user(difficulty):
    try:
        l = input("Please enter the list of numbers u saw in the length of " + str(difficulty) + " items: ")
        s = l.split()
        list = [int(item) for item in s]
        return list
    except ValueError as e:
        print("The error is... " + str(e.__class__) + "\nPlease enter only numbers.")




def is_list_equal(difficulty):
   return generate_sequence(difficulty) == get_list_from_user(difficulty)


def play(difficulty):
    return is_list_equal(difficulty)
