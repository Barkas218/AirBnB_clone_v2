#!/usr/bin/python3
from flask import Flask
from models import storage
from models import State
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def show_states_list():
    """ Gets states list """
    state_l = storage.all('State')
    return render_template('7-states_list.html', state_l=state_l)


@app.route('/hbnb_filters', strict_slashes=False)
def show_filters():
    """ Shows states id """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

@app.teardown_appcontext
def tear_down_db(n):
    """ Closes the sql session """
    storage.close()


if __name__ == '__main__':
    app.run()
