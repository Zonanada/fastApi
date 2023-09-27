from core.models.general_db import session, Submenu, Dishes, uuid4
from fastapi import HTTPException
from sqlalchemy import func, select

def to_dict_submenu(sqlalchemy_list):
        return {"id":sqlalchemy_list[0], "title":sqlalchemy_list[1], "description":sqlalchemy_list[2], "dishes_count": sqlalchemy_list[3]}

class SubmenuRepository():
    
    def get(**kwargs):
        try:
            if (("submenu_id" in kwargs) == False):
                return session.query(Submenu).filter(Submenu.menu_id == kwargs["menu_id"]).all()
            
            
            query = select(Submenu.id, Submenu.title, Submenu.description,
                    func.count(Dishes.id.distinct()))\
                    .outerjoin(Dishes, Submenu.id == Dishes.submenu_id)\
                    .where(Submenu.id == kwargs["submenu_id"]).group_by(Submenu.id)
            return to_dict_submenu(session.execute(query).first())
        
        except:
            raise HTTPException(status_code=404, detail="submenu not found")
        
    def insert(menu_id: str, query):
        try:
            submenu = Submenu(id=str(uuid4()), menu_id=menu_id, title=query.title, description=query.description)
            session.add(submenu)
            session.commit()
            session.refresh(submenu)
            return submenu
        except:
            raise HTTPException(status_code=404, detail="submenu not found")

    def update(submenu_id, query):
        try:
            submenu = session.query(Submenu).filter(Submenu.id == submenu_id).first()
            submenu.title = query.title
            submenu.description = query.description
            session.commit()
            query = select(Submenu.id, Submenu.title, Submenu.description,
                    func.count(Dishes.id.distinct()))\
                    .outerjoin(Dishes, Submenu.id == Dishes.submenu_id)\
                    .where(Submenu.id == submenu_id).group_by(Submenu.id)
            return to_dict_submenu(session.execute(query).first())
        except:
            raise HTTPException(status_code=404, detail="submenu not found")

    def delete(submenu_id):
        try:
            submenu = session.query(Submenu).filter(Submenu.id == submenu_id).first()
            session.query(Dishes).filter(Dishes.submenu_id == submenu_id).delete(synchronize_session='fetch')
            session.delete(submenu)
            session.commit()
            return {"status": True, "message": "The submenu has been deleted"}
        except:
            raise HTTPException(status_code=404, detail="submenu not found")
