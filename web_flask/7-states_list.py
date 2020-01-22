#!/usr/bin/python3
"""
script that starts a Flask web applicatio
"""


from models import storage
from model.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def tdown(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    st = storage.all(State)
    return render_template('7-states_list.html', st=st)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)