from flask import Flask, render_template
from Utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, "r") as f:
            score = f.read()
        return render_template('Score.html', SCORE=score)
    except FileNotFoundError as f:
        score = f'{f.args[1]}: {f.filename}\n'
        return render_template('Error.html', SCORE=score)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
