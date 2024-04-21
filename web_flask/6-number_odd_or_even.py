#!/usr/bin/python3
"A moudle that  a script that starts a Flask web application"
from flask import render_template


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    "A module that print a even or odd number"
    result = "even" if n % 2 == 0 else "odd"
    return render_template('number_odd_or_even.html', n=n, result=result)
