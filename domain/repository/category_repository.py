from abc import ABC

from domain.model.category_domain import Category_domain


class Category_repository(ABC):
    def get_all(self):
        raise NotImplemented

    def find_by_name(self, name: str):
        raise NotImplemented
