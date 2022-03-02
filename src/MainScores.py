from flask import Flask, render_template
from Utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, "r") as f:
            SCORE = f.read()
        return render_template('Score.html', SCORE=SCORE)
    except FileNotFoundError as f:
        SCORE = f'{f.args[1]}: {f.filename}\n'
        return render_template('Error.html', SCORE=SCORE)


if __name__ == '__main__':
    app.run()