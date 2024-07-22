from abc import ABC

from domain.model.category_domain import Category_domain
from domain.repository.category_repository import Category_repository
from infraestructure.configuration.db import SessionLocal
from infraestructure.mappers.mapper_service import Category_mapper_service
from infraestructure.schema.models_factory import Category


class Category_repository_impl(Category_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(Category).all()

    def find_by_name(self, name: str):
        category = self.db.query(Category).filter(Category.name == name).first()
        return category.uuid

    def has_categories(self):
        return self.db.query(Category).count() > 0
