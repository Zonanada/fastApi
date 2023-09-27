from core.models.general_db import session, Dishes, uuid4
from fastapi import HTTPException


class DishesRepository:
    def get(**args):
        if ("dish_id" in args) == False:
            return session.query(Dishes).filter(Dishes.submenu_id == args["submenu_id"]).all()
        result = session.query(Dishes).filter(Dishes.id == args["dish_id"]).first()
        if (result == None):
            raise HTTPException(status_code=404, detail="dish not found")
        return result
        

    def inser(submenu_id, query):
        dish = Dishes(id=str(uuid4()),  submenu_id=submenu_id, title=query.title, description=query.description, price=query.price)
        session.add(dish)
        session.commit()
        session.refresh(dish)
        return dish

    def update(dish_id, query):
        try:
            dish = session.query(Dishes).filter(Dishes.id == dish_id).first()
            dish.title = query.title
            dish.description = query.description
            dish.price = query.price
            session.commit()
            session.refresh(dish)
            return dish
        except:
            raise HTTPException(status_code=404, detail="dish not found")

    def delete(dish_id):
        try:
            dishes = session.query(Dishes).filter(Dishes.id == dish_id).first()
            session.delete(dishes)
            session.commit()
            return {"status": True, "message": "The dish has been deleted"}
        except:
            raise HTTPException(status_code=404, detail="dish not found")
