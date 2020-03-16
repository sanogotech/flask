# Flask
Python  Web  Flask 

## MVC

##  Request
 * https://flask.palletsprojects.com/en/1.1.x/quickstart/

username = request.form['username']
password = request.form['password']
*************************
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
  
  ************
  <!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}

# Form

## Flash Message
flash(u'Profile successfully created')

## Template /Jinja

## Session

## OpenID

- https://pythonhosted.org/Flask-OpenID/

- https://github.com/sanogotech/flask-openid

## ORM / SQLAlchemy

## Cache

## Logs

## Tests
