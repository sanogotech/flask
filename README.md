# Flask
Python  Web  Flask 

## MVC

##  Request
https://flask.palletsprojects.com/en/1.1.x/quickstart/
username = request.form['username']
password = request.form['password']

*************  home.html ************
```
<!doctype html>
<form action="/hello">
  <label for="nom">Nom :</label><br>
  <input type="text" id="nom" name="nom"><br>
   <input type="submit" value="Submit">
</form>
```
*************  hello.py ************
```
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<nom>')
def hello(name=None):
    return render_template('hello.html', nom=nom)
  ```
  ******  hello.html ******
  ```
  <!doctype html>
<title>Hello from Flask</title>
{% if nom %}
  <h1>Bonjour  {{ nom }}!</h1>
{% else %}
  <h1>Bonjour, Abidjan !</h1>
{% endif %}
```
# Form

## Flash Message
flash(u'Profile successfully created')

## Template /Jinja

## Session

## OpenID
https://pythonhosted.org/Flask-OpenID/
https://github.com/sanogotech/flask-openid

## ORM / SQLAlchemy

## Cache

## Logs

## Tests
