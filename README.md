''' LARGE FLASK APP REQUIRE A LOT OF  MODULARIZATION '''

LARGE APP == FACTORY + BLUEPRINTS +SERVICES + EXTENSIONS
1. Factory build the app.
2. Blueprints are departments: Auth Admin etc
3. Services are workers: They do logics.( Not the Routes)
4. Models are database.
5. Config  is settings.

NOTE: Never put business logic in routes. Routes only receive request, call service, return response.

*** IF folder has >10 files split.
1. factory Pattern
app> __init__.py 
  used to register the app
  then run.py to run the app

2. Config
Microsoft Windows [Version 10.0.22631.6199]


 python.exe -m pip install --upgrade pip


Successfully installed pip-26.3

pip install python-dotenv
Collecting python-dotenv
 

pip install -U Flask-SQLAlchemy

pip install flask-login
pip install Flask-Migrate


>pip install Flask-Caching


