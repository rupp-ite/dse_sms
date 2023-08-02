from app.models import *

def insert_menu():
    menus=[Menu(name_latin='Setting',order=1),Menu(name_latin='Student',order=2)]
    db.session.add_all(menus)
    db.session.commit()
    
def insert_sub_menu():
    sub_menus=[SubMenu(menu_id=1,name_latin='User',order=1,end_point='e01'),\
            SubMenu(menu_id=1,name_latin='Password',order=2,end_point='e02'),\
            SubMenu(menu_id=2,name_latin='Dashboard',order=1,end_point='e03'),\
            SubMenu(menu_id=2,name_latin='Course',order=2,end_point='e04')
        ]
    db.session.add_all(sub_menus)
    db.session.commit()