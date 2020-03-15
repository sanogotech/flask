# Flask
Python  Web  Flask 

## MVC

##  Request
https://flask.palletsprojects.com/en/1.1.x/quickstart/
https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

*************  home.html ************
```
<!doctype html>
<form action="/hello">
  <label for="nom">Nom :</label><br>
  <input type="text" id="nom" name="nom"><br>
  
  <label for="prenom">Prénom :</label><br>
  <input type="text" id="prenom" name="prenom"><br>
  
   <input type="submit" value="Submit">
</form>
```
*************  hello.py ************
```
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<nom>')
def hello(name=None):
    prenom = request.args['prenom']   #if key doesn't exist, returns a 400, bad request error
    nom =  request.args.get('nom')   #if key doesn't exist, returns None
    return render_template('hello.html', nom=nom)
  ```
 
```
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']
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

# Flask  Run Main Paramaters
```
if _name == '__main_':
    app.run(debug=True, port=5000,host='locahhost', reload=True)

```
