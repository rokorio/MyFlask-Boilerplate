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
(c) Microsoft Corporation. All rights reserved.

C:\Users\LITIGTION USER\Desktop\mprojo\myapp>python -m venv .venv

C:\Users\LITIGTION USER\Desktop\mprojo\myapp>"c:\Users\LITIGTION USER\Desktop\mprojo\myapp\.venv\Scripts\activate"

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>pip install flask
Collecting flask
  Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting blinker>=1.9.0 (from flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.5.1-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask)
  Downloading markupsafe-3.0.4-cp314-cp314-win_amd64.whl.metadata (2.8 kB)
Collecting werkzeug>=3.1.0 (from flask)
  Downloading werkzeug-3.1.9-py3-none-any.whl.metadata (4.1 kB)
Downloading flask-3.1.3-py3-none-any.whl (103 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.5.1-py3-none-any.whl (126 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading markupsafe-3.0.4-cp314-cp314-win_amd64.whl (14 kB)
Downloading werkzeug-3.1.9-py3-none-any.whl (228 kB)
Installing collected packages: markupsafe, itsdangerous, click, blinker, werkzeug, jinja2, flask
Successfully installed blinker-1.9.0 click-8.5.1 flask-3.1.3 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.4 werkzeug-3.1.9

[notice] A new release of pip is available: 25.3 -> 26.3
[notice] To update, run: python.exe -m pip install --upgrade pip

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>python -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\litigtion user\desktop\mprojo\myapp\.venv\lib\site-packages (25.3)
Collecting pip
  Downloading pip-26.3-py3-none-any.whl.metadata (4.6 kB)
Downloading pip-26.3-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 8.8 MB/s  0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.3
    Uninstalling pip-25.3:
      Successfully uninstalled pip-25.3
Successfully installed pip-26.3

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>pip install python-dotenv
Collecting python-dotenv
  Downloading python_dotenv-1.2.4-py3-none-any.whl.metadata (29 kB)
Downloading python_dotenv-1.2.4-py3-none-any.whl (23 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.2.4

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>pip install -U Flask-SQLAlchemy
Collecting Flask-SQLAlchemy
  Downloading flask_sqlalchemy-3.1.1-py3-none-any.whl.metadata (3.4 kB)
Requirement already satisfied: flask>=2.2.5 in .\.venv\Lib\site-packages (from Flask-SQLAlchemy) (3.1.3)
Collecting sqlalchemy>=2.0.16 (from Flask-SQLAlchemy)
  Downloading sqlalchemy-2.1.8-cp314-cp314-win_amd64.whl.metadata (9.9 kB)
Requirement already satisfied: blinker>=1.9.0 in .\.venv\Lib\site-packages (from flask>=2.2.5->Flask-SQLAlchemy) (1.9.0)
Requirement already satisfied: click>=8.1.3 in .\.venv\Lib\site-packages (from flask>=2.2.5->Flask-SQLAlchemy) (8.5.1)
Requirement already satisfied: itsdangerous>=2.2.0 in .\.venv\Lib\site-packages (from flask>=2.2.5->Flask-SQLAlchemy) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in .\.venv\Lib\site-packages (from flask>=2.2.5->Flask-SQLAlchemy) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in .\.venv\Lib\site-packages (from flask>=2.2.5->Flask-SQLAlchemy) (3.0.4)
Requirement already satisfied: werkzeug>=3.1.0 in .\.venv\Lib\site-packages (from flask>=2.2.5->Flask-SQLAlchemy) (3.1.9)
Collecting typing-extensions>=4.6.0 (from sqlalchemy>=2.0.16->Flask-SQLAlchemy)
  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Downloading flask_sqlalchemy-3.1.1-py3-none-any.whl (25 kB)
Downloading sqlalchemy-2.1.8-cp314-cp314-win_amd64.whl (2.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 7.5 MB/s  0:00:00
Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Installing collected packages: typing-extensions, sqlalchemy, Flask-SQLAlchemy
Successfully installed Flask-SQLAlchemy-3.1.1 sqlalchemy-2.1.8 typing-extensions-4.16.0

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>pip install flask-login
Collecting flask-login
  Downloading Flask_Login-0.6.3-py3-none-any.whl.metadata (5.8 kB)
Requirement already satisfied: Flask>=1.0.4 in .\.venv\Lib\site-packages (from flask-login) (3.1.3)
Requirement already satisfied: Werkzeug>=1.0.1 in .\.venv\Lib\site-packages (from flask-login) (3.1.9)
Requirement already satisfied: blinker>=1.9.0 in .\.venv\Lib\site-packages (from Flask>=1.0.4->flask-login) (1.9.0)
Requirement already satisfied: click>=8.1.3 in .\.venv\Lib\site-packages (from Flask>=1.0.4->flask-login) (8.5.1)
Requirement already satisfied: itsdangerous>=2.2.0 in .\.venv\Lib\site-packages (from Flask>=1.0.4->flask-login) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in .\.venv\Lib\site-packages (from Flask>=1.0.4->flask-login) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in .\.venv\Lib\site-packages (from Flask>=1.0.4->flask-login) (3.0.4)
Downloading Flask_Login-0.6.3-py3-none-any.whl (17 kB)
Installing collected packages: flask-login
Successfully installed flask-login-0.6.3

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>pip install Flask-Migrate
Collecting Flask-Migrate
  Downloading Flask_Migrate-4.1.0-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: Flask>=0.9 in .\.venv\Lib\site-packages (from Flask-Migrate) (3.1.3)
Requirement already satisfied: Flask-SQLAlchemy>=1.0 in .\.venv\Lib\site-packages (from Flask-Migrate) (3.1.1)
Collecting alembic>=1.9.0 (from Flask-Migrate)
  Downloading alembic-1.20.1-py3-none-any.whl.metadata (7.3 kB)
Requirement already satisfied: SQLAlchemy>=2.0 in .\.venv\Lib\site-packages (from alembic>=1.9.0->Flask-Migrate) (2.1.8)
Collecting Mako (from alembic>=1.9.0->Flask-Migrate)
  Downloading mako-1.4.3-py3-none-any.whl.metadata (2.9 kB)
Requirement already satisfied: typing-extensions>=4.12 in .\.venv\Lib\site-packages (from alembic>=1.9.0->Flask-Migrate) (4.16.0)
Requirement already satisfied: blinker>=1.9.0 in .\.venv\Lib\site-packages (from Flask>=0.9->Flask-Migrate) (1.9.0)
Requirement already satisfied: click>=8.1.3 in .\.venv\Lib\site-packages (from Flask>=0.9->Flask-Migrate) (8.5.1)
Requirement already satisfied: itsdangerous>=2.2.0 in .\.venv\Lib\site-packages (from Flask>=0.9->Flask-Migrate) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in .\.venv\Lib\site-packages (from Flask>=0.9->Flask-Migrate) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in .\.venv\Lib\site-packages (from Flask>=0.9->Flask-Migrate) (3.0.4)
Requirement already satisfied: werkzeug>=3.1.0 in .\.venv\Lib\site-packages (from Flask>=0.9->Flask-Migrate) (3.1.9)
Downloading Flask_Migrate-4.1.0-py3-none-any.whl (21 kB)
Downloading alembic-1.20.1-py3-none-any.whl (270 kB)
Downloading mako-1.4.3-py3-none-any.whl (80 kB)
Installing collected packages: Mako, alembic, Flask-Migrate
Successfully installed Flask-Migrate-4.1.0 Mako-1.4.3 alembic-1.20.1

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>pip install Flask-Caching
Collecting Flask-Caching
  Downloading flask_caching-2.5.1-py3-none-any.whl.metadata (2.0 kB)
Requirement already satisfied: flask>=3.0 in .\.venv\Lib\site-packages (from Flask-Caching) (3.1.3)
Collecting cachelib>=0.17.0 (from Flask-Caching)
  Downloading cachelib-0.17.2-py3-none-any.whl.metadata (3.5 kB)
Requirement already satisfied: blinker>=1.9.0 in .\.venv\Lib\site-packages (from flask>=3.0->Flask-Caching) (1.9.0)
Requirement already satisfied: click>=8.1.3 in .\.venv\Lib\site-packages (from flask>=3.0->Flask-Caching) (8.5.1)
Requirement already satisfied: itsdangerous>=2.2.0 in .\.venv\Lib\site-packages (from flask>=3.0->Flask-Caching) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in .\.venv\Lib\site-packages (from flask>=3.0->Flask-Caching) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in .\.venv\Lib\site-packages (from flask>=3.0->Flask-Caching) (3.0.4)
Requirement already satisfied: werkzeug>=3.1.0 in .\.venv\Lib\site-packages (from flask>=3.0->Flask-Caching) (3.1.9)
Downloading flask_caching-2.5.1-py3-none-any.whl (35 kB)
Downloading cachelib-0.17.2-py3-none-any.whl (35 kB)
Installing collected packages: cachelib, Flask-Caching
Successfully installed Flask-Caching-2.5.1 cachelib-0.17.2

(.venv) C:\Users\LITIGTION USER\Desktop\mprojo\myapp>