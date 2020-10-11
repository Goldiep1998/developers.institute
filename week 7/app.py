from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/<name>')
def user(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run()