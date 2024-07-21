from sqlalchemy.orm import Session
from infraestructure.configuration.db import engine
from infraestructure.schema.models_factory import Category


def seed_categories():
    session = Session(engine)

    categories = [
        {"name": "Comercio"},
        {"name": "Restaurante"},
        {"name": "Bar"},
        {"name": "Servicios varios"},
        {"name": "Salud"},
        {"name": "Educación"},
        {"name": "Entretenimiento"},
        {"name": "Deportes"},
        {"name": "Cultura"},
        {"name": "Turismo"},
        {"name": "Hogar"},
        {"name": "Moda"},
        {"name": "Tecnología"},
        {"name": "Automóviles"},
        {"name": "Mascotas"},
        {"name": "Belleza"},
    ]

    for category in categories:
        category_obj = Category(**category)
        session.add(category_obj)

    session.commit()


seed_categories()
