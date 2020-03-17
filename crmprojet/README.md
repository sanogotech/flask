#  Flask in 3h 
https://youtu.be/3mwFC4SHY-Y

# pip install python-dotenv 
python-dotenv  can be used in your Flask project to make handling Flask CLI configuration and general app configuration more convenient.

- How to use Python-dotenv for Flask development server options. -.flaskenv
- How to use Python-dotenv for application specific configuration. - .env
- How to use it in production. - gunicorn

##  .flaskenv
FLASK_APP=app.py
FLASK_ENV=development
FLASK_ENV - Controls the environment.
FLASK_DEBUG - Enables debug mode.
FLASK_RUN_EXTRA_FILES - A list of files that will be watched by the reloader in addition to the Python modules.
FLASK_RUN_HOST - The host you want to bind your app to.
FLASK_RUN_PORT - The port you want to use.
FLASK_RUN_CERT - A certificate file for so your app can be run with HTTPS.
FLASK_RUN_KEY - The key file for your cert.

## #.env
SECRET_KEY=topsecretkey
API_KEY=donotsharethisapikeywithanyone

## Running in Production
pipenv install gunicorn

## Web Doc  
https://prettyprinted.com/tutorials/automatically_load_environment_variables_in_flask

https://realpython.com/flask-by-example-part-1-project-setup/

##  Code Sample
https://github.com/dibstern/flask_proj



