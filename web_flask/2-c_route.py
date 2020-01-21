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
def hello_3(text):
    s = 'C {}'.format(escape(text))
    s = s.replace("_", " ")
    return s


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
