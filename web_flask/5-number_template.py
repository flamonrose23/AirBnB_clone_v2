#!/usr/bin/python3
"""
Writing script starting Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returning Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returning HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Displaying “C ” followed by value of text variable
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    Displaying “Python ”, followed by value of text variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """
    Displaying “n is a number” only if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """
    Displaying HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
