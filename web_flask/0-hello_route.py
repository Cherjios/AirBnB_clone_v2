#!/usr/bin/python3
"""
script that starts a Flask web applicatio
"""


from flask import Flask
app = Fask(__name__)


@app.router("/, strict_slashes=False")
def hello_HBNB():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
