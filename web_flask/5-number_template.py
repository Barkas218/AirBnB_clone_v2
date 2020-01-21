#!/usr/bin/python3
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns hello holberton """
    hello = 'Hello HBNB!'
    return hello


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ Shows hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_is_fun(text):
    """ Cs is fun jeje """
    rep_text = text.replace("_", " ")
    return 'C %s' % rep_text


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def show_python_is_cool(text):
    """ Python is cool """
    rep_text = text.replace("_", " ")
    return 'Python %s' % rep_text


@app.route('/number/<int:n>', strict_slashes=False)
def show_int(n):
    """ shows an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_template_n(n):
    """ Shows a template if integer """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
