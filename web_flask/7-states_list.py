#!/usr/bin/python3
from flask import Flask
from models import storage
from models import State
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def show_states_list():
    """ Gets states list """
    states_l = storage.all(State)
    return render_template('7-states_list.html', states_l=states_l)




@app.teardown_appcontext
def tear_down_db():
    """ Closes the sql session """
    storage.close()
