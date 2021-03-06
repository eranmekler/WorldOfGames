import os
from src.Utils import SCORES_FILE_NAME, SCORES_FILE_NAME_PATH

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    exists = os.path.isfile(SCORES_FILE_NAME)

    if exists:
        with open(SCORES_FILE_NAME, "r") as f:
            current_score = int(f.read())
        with open(SCORES_FILE_NAME, "w") as f:
            f.write(str(points_of_winning + current_score))
            f.close()
    else:
        with open(SCORES_FILE_NAME_PATH, "w") as f:
            f.write(str(points_of_winning))
            f.close()
