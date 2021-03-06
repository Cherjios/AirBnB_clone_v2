#!/usr/bin/python3
"""
script that starts a Flask web applicatio
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State

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
