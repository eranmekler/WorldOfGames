import os

SCORES_FILE_NAME = "src/Scores.txt"
SCORES_FILE_NAME_PATH = "src/Scores.txt"
BAD_RETURN_CODE = -1

def cls():
    os.system('cls' if os.name =='nt' else 'clear')
