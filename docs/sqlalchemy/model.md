# Models
- In Flask-SQLAlchemy, a "model" refers to a Python class that represents a database table.
- In traditional relational databases, tables are used to store data. Each table has columns (fields) that define the structure of the data it holds. In Flask-SQLAlchemy, you define these tables as Python classes, and each attribute of the class represents a column in the table.


| Ojbect Name       |   Description |
|-------------------|---------------|
| Integer           | an integer    |
| String(size)      | a string with a maximum length (optional in some databases, e.g. PostgreSQL)|
| Text              |some longer unicode text|
| DateTime          |date and time expressed as Python datetime object.|
| Float             |stores floating point values|
| Boolean           |stores a boolean value|
|PickleType         |stores a pickled Python object|
|LargeBinary        |stores large arbitrary binary data|

## Relationship
- In SQLAlchemy, both 'back_populates' and 'backref' are used to define bidirectional relationships between models.
- 'back_populates': Requires explicitly defining the relationship in both models using db.relationship and specifying back_populates to establish the bidirectional link
- 'backref': Automatically sets up the reverse relationship using the backref argument in one of the models. You only need to specify the relationship in one model, and SQLAlchemy handles the creation of the complementary attribute in the other model.
### 1. One-to-Many Relationships
### 2. One-to-One Relationships
### 3. Many-to-Many Replationships