## INSERT DATA INTO TABLE
#### 1. Insert a new record into a table
- Option 1

        >>> from app.models.student import Student
        >>> s1 = Student()
        >>> s1.first_name = "Bunchhun"
        >>> s1.last_name = "Chhim"
        >>> s1.email = "chhim.bunchhun@rupp.edu.kh"
        >>> s1.age = 30
        >>> db.session.add(s1)
        >>> db.session.commit()
- Option 2

        >>> from app.models.student import Student
        >>> s2 = Student(first_name='Bunchhun2',last_name='Chhim2',email='chhim.bunchhun2@rupp.edu.kh',age=30)
        >>> db.session.add(s2)
        >>> db.session.commit()
#### 2 Insert multiple rows into a table
##### Option 1: session.bulk_insert_mappings()
        
        >>> from app.models.student import Student
        >>> data = [{'first_name':'Dara1','last_name':'Sok','email':'sok.dara@rupp.edu.kh','age':35},{'first_name':'Dara2','last_name':'Sok','email':'sok.dara2@rupp.edu.kh','age':40}]
        >>> db.session.bulk_insert_mappings(Student,data)
        >>> db.session.commit()
##### Option 2:session.add_all()
        
        >>> students = [Student(first_name='Sok1',last_name='Pisey',email='sok1@rupp.edu.kh',age=24), Student(first_name='Sok2',last_name='Pisey',email='sok2@rupp.edu.kh',age=25)]
        >>> db.session.add_all()
        >>> db.session.commit()