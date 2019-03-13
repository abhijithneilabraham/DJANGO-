from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Stuck at home in a beautiful ectsasy"

if __name__ == '__main__':
    app.run()