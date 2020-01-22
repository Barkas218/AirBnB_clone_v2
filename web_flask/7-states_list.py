#!/usr/bin/python3
from flask import Flask
from models import storage
from models import State
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def show_states_list():
    """ Gets states list """
    state_l = storage.all('State')
    return render_template('7-states_list.html', state_l=state_l)


@app.teardown_appcontext
def tear_down_db(n):
    """ Closes the sql session """
    storage.close()


if __name__ == '__main__':
    app.run()
