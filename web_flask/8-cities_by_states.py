#!/usr/bin/python3
from flask import Flask
from models import storage
from models import State
from flask import render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def show_states_list():
    """ Gets states list """
    state_l = storage.all('State')
    return render_template('8-cities_by_states.html', state_l=state_l)


@app.teardown_appcontext
def tear_down_db(n):
    """ Closes the sql session """
    storage.close()


if __name__ == '__main__':
    app.run()
