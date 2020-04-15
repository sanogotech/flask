# Flask in Action

## 1. Installing  Flask

```
pip install Flask
```

## 2. Flask hello world app

Create a file called hello.py

```python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
     return "Hello World!"

if __name__ == "__main__":
    app.run()
```
Finally run the web app using this command:
```
$ python hello.py
* Running on http://localhost:5000/
```

Open http://localhost:5000/ in your webbrowser, and “Hello World!” should appear

## 3. Render Template Page (Next Step)



