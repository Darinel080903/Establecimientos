from abc import ABC

from domain.model.dto.response.base_response import Base_response
from domain.model.establishment_domain import Establishment_domain
from domain.repository.category_repository import Category_repository
from domain.repository.establishment_repository import Establishment_repository
from domain.repository.service_respository import Service_repository
from domain.use_case.establishment_use_case import Establishment_use_case


class Establishment_service(Establishment_use_case, ABC):
    def __init__(self, establishment_repository: Establishment_repository, category_repository: Category_repository, service_response: Service_repository):
        self.establishment_repository = establishment_repository
        self.category_repository = category_repository
        self.service_response = service_response

    def get_all(self) -> Base_response:
        try:
            establishments = self.establishment_repository.get_all()
            return Base_response(data=establishments, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def add_establishment(self, establishment: Establishment_domain, user_id: str) -> Base_response:
        name = establishment.category
        category_uuid = self.category_repository.find_by_name(name)
        establishment.category = category_uuid
        establishment.user_id = user_id
        services = establishment.services
        id_new = establishment.uuid
        establishment = self.establishment_repository.add_establishment(establishment)
        print(establishment.services.__str__())
        establishment.services = self.service_response.add_service(services, id_new)
        return Base_response(data=establishment, message="Success", code=201)

    def update_establishment(self, establishment: Establishment_domain, establishment_id: str) -> Base_response:
        try:
            establishment = self.establishment_repository.update_establishment(establishment, establishment_id)
            return Base_response(data=establishment, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def delete_establishment(self, establishment_id: str) -> Base_response:
        try:
            self.establishment_repository.delete_establishment(establishment_id)
            return Base_response(data=None, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_uuid(self, uuid: str) -> Base_response:
        try:
            establishment = self.establishment_repository.get_by_uuid(uuid)
            return Base_response(data=establishment, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_category(self, category: str) -> Base_response:
        try:
            establishments = self.establishment_repository.get_by_category(category)
            return Base_response(data=establishments, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_user(self, user_id: str) -> Base_response:
        try:
            establishments = self.establishment_repository.get_by_user(user_id)
            return Base_response(data=establishments, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_categories(self):
        try:
            categories = self.category_repository.get_all()
            return Base_response(data=categories, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)
