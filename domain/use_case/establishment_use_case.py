from abc import ABC, abstractmethod

from domain.model.dto.response.base_response import Base_response
from domain.model.establishment_domain import Establishment_domain
from domain.repository.category_repository import Category_repository
from domain.repository.establishment_repository import Establishment_repository
from domain.repository.service_respository import Service_repository


class Establishment_use_case(ABC):
    @abstractmethod
    def __init__(self, establishment_repository: Establishment_repository, category_repository: Category_repository, service_response: Service_repository):
        self.establishment_repository = establishment_repository
        self.category_repository = category_repository
        self.service_response = service_response

    @abstractmethod
    def get_all(self) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def add_establishment(self, establishment: Establishment_domain, user_id: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def update_establishment(self, establishment: Establishment_domain, establishment_id: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def delete_establishment(self, establishment_id: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_by_uuid(self, uuid: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_by_category(self, category: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_by_user(self, user_id: str) -> Base_response:
        raise NotImplemented

    @abstractmethod
    def get_categories(self):
        raise NotImplemented

    @abstractmethod
    def add_portrait_image(self, content: bytes, filename: str, uuid_establishment: str) -> Base_response:
        raise NotImplemented
