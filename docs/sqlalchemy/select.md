## Retrieving Data from the Database
#### 1. Retrieving All Records

    Use the all() method on the query attribute to get all the records in a table
    >>> from app.models.student import Student
    >>> q=Student.query.all()
#### 2. Sorting the result

    Use order_by() method to sort the result
    >>> Student.query.order_by(Student.id.desc()).all()
    >>> Student.query.order_by(Student.id.asc()).all()
#### 3. Retrieving the First Record
    
    Use the first() method to get the first record
    >>> Student.query.order_by(Student.id.desc()).first()
#### 4. Retrieving a record by ID

    When records are identified with a unique ID, use get() method to fetch a record by its ID
    >>> Student.query.get(1) #legacy as of the 1.x series of SQLAlchemy
    >>> db.session.get(Student,1)
#### 5. Retrieving a Record or Multiple Records by a Column Value
* filter_by() is used for simple queries on the column names using regular kwargs, like db.users.filter_by(name='Joe')
* The same can be accomplished with filter(), not using kwargs, but instead using the '==' equality operator

        >>> Student.query.filter_by(first_name='Bunchhun').all()
        >>> Student.query.filter(Student.age>30).all()
