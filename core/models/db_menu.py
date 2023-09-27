from core.models.general_db import Menu, session, Submenu, Dishes, uuid4
from fastapi import HTTPException
from sqlalchemy import func, select


def to_dict_menu(sqlalchemy_list):
    return {"id": sqlalchemy_list[0], "title": sqlalchemy_list[1], "description": sqlalchemy_list[2], "submenus_count": sqlalchemy_list[3], "dishes_count": sqlalchemy_list[4]}


def to_dict_menu_list(sqlalchemy_list):
    result = list()
    for item in sqlalchemy_list:
        result.append(to_dict_menu(item))
    return result


class MenuRepository():
    def insert(query):
        menu = Menu(id=str(uuid4()), title=query.title, description=query.description)
        session.add(menu)
        session.commit()
        session.refresh(menu)
        return menu

    def get(**kwargs):
        try:
            if (("menu_id" in kwargs) == False):

                query = select(Menu.id, Menu.title, Menu.description,
                               func.count(Submenu.id.distinct()), func.count(Dishes.id.distinct()))\
                    .outerjoin(Submenu, Submenu.menu_id == Menu.id)\
                    .outerjoin(Dishes, Submenu.id == Dishes.submenu_id)\
                    .group_by(Menu.id)
                return to_dict_menu_list(session.execute(query))


            query = select(Menu.id, Menu.title, Menu.description,
                           func.count(Submenu.id.distinct()), func.count(Dishes.id.distinct()))\
                .outerjoin(Submenu, Submenu.menu_id == Menu.id)\
                .outerjoin(Dishes, Submenu.id == Dishes.submenu_id)\
                .where(Menu.id == kwargs["menu_id"]).group_by(Menu.id)
            return to_dict_menu(session.execute(query).first())

        except:
            raise HTTPException(status_code=404, detail="menu not found")

    def update(menu_id: str, query):
        try:
            menu = session.query(Menu).filter(Menu.id == menu_id).first()
            menu.title = query.title
            menu.description = query.description
            session.commit()

            query = select(Menu.id, Menu.title, Menu.description,
                           func.count(Submenu.id.distinct()), func.count(Dishes.id.distinct()))\
                .outerjoin(Submenu, Submenu.menu_id == Menu.id)\
                .outerjoin(Dishes, Submenu.id == Dishes.submenu_id)\
                .where(Menu.id == menu_id).group_by(Menu.id)
            result = to_dict_menu(session.execute(query).first())
            return result
        except:
            raise HTTPException(status_code=404, detail="menu not found")

    def delete(menu_id: str):
        try:
            menu = session.query(Menu).filter(Menu.id == menu_id).first()
            session.delete(menu)
            session.query(Submenu).filter(Submenu.menu_id ==
                                          menu_id).delete(synchronize_session='fetch')
            session.commit()
            return {"status": True, "message": "The menu has been deleted"}
        except:
            raise HTTPException(status_code=404, detail="menu not found")
