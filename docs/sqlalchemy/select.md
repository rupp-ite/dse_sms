## Retrieving Data from the Database
#### 1. Query all records

    Use the all() method on the query attribute to get all the records in a table
    >>> from app.models import Student
    >>> q=Student.query.all()
#### 2. Sorting the result

    Use order_by() method to sort the result
    >>> Student.query.order_by(Student.id.desc()).all()
    >>> Student.query.order_by(Student.id.asc()).all()
#### 3. Query the first record
    
    Use the first() method to get the first record
    >>> Student.query.order_by(Student.id.desc()).first()
#### 4. Query a record by its primary key (ID)

    When records are identified with a unique ID, use get() method to fetch a record by its ID
    >>> Student.query.get(1) #legacy as of the 1.x series of SQLAlchemy
    >>> db.session.get(Student,1)
#### 5. Query records based on a filter
* filter_by() is used for simple queries on the column names using regular kwargs, like db.users.filter_by(name='Joe')
* The same can be accomplished with filter(), not using kwargs, but instead using the '==' equality operator

        >>> Student.query.filter_by(first_name='Bunchhun').all()
        >>> Student.query.filter(Student.age>30).all()

# Using join
### two tables
    mm=db.session.query(sys_menu,sys_menumodule).join(sys_menumodule, sys_menu.sys_menumodule_id==sys_menumodule.id).with_entities(sys_menu.id, sys_menu.name_latin, sys_menumodule.name_latin).all()
### multiple
    q = db.session.query(Survey, Person, Question, Answer)
                  .filter(Person.survey_id == Survey.survey_id,
                          Question.survey_id == Survey.survey_id,
                          Answer.question_id == Question.question_id).all()
    print(q)

### menu
    def mm_dict():
        lmm=[]
        #get distinct menu_id which exist in submenu records
        m_id=db.session.query(sys_submenu, sys_menu).join(sys_menu,sys_submenu.sys_menu_id==sys_menu.id)\
            .with_entities(sys_submenu.sys_menu_id).filter(sys_menu.sys_menumodule_id==1).distinct().all()
    
        #m_id=db.session.query(sys_submenu.sys_menu_id).distinct().all()
        for u in db.session.query(sys_menu.id, sys_menu.code, sys_menu.name_latin, sys_menu.name_khmer, sys_menu.order, sys_menu.icon_class).\
                filter(sys_menu.id.in_(m_id)).order_by(sys_menu.order):
            lsm = []
            for v in db.session.query(sys_submenu, sys_template).join(sys_template, sys_submenu.sys_template_id==sys_template.id)\
                .with_entities(sys_submenu.id,sys_submenu.name_latin,sys_submenu.name_khmer,sys_submenu.code,sys_template.path, sys_submenu.order, sys_submenu.icon_class) \
                .filter(sys_submenu.sys_menu_id == u.id).order_by(sys_submenu.order):
                lsm.append(v._asdict())
            m=u._asdict()
            m['sub'] = tuple(lsm)
            lmm.append(m)
        return lmm
    
    @AdminApp.route('/admin/menu/')
    #@login_required
    def admin_menu():
        navigation = mm_dict()
        return render_template('admin_menu.html', navigation_bar=navigation)