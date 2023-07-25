### How to test sqlalchmey(db) in interactive shell
- Enter into interactive shell:
    (venv)->Python
    >>> from app import db, create_app
    >>> app=create_app()
    >>> db.app=app
    >>> db.create_all()
    >>> app.app_context().push()
- import models, example:
        
        >>> from app.models.student import Student
- Run query

        >>> Student.query.all()