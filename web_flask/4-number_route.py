#!/usr/bin/python3
"""
script that starts a Flask web applicatio
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_2():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(escape(n))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
