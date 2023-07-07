### How to test sqlalchmey(db) in interactive shell
- Enter into interactive shell:
    ``(venv)->Python``
- import db, create_app from app
    ```>>> from app import db, create_app```
- create app
    ```>>> app=create_app()```
- set db.app=app
    ```>>> db.app=app```
- run db.create_all()
    ```>>> db.create_all()```
- import models, example:
    ```>>> from app.admin.models import sys_menu, sys_menumodule```
- Run query
    ```>>> sys_menu.query.all()```
    ```>>> sys_menumodule.query.all()```