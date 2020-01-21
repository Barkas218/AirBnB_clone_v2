#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns hello holberton """
    hello = 'Hello HBNB!'
    return (hello)


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ Shows hbnb """
    return ('HBNB')


if __name__ == '__main__':
    app.run()
