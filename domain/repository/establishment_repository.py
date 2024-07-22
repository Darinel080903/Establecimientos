from abc import ABC, abstractmethod

from domain.model.establishment_domain import Establishment_domain


class Establishment_repository(ABC):
    @abstractmethod
    def get_all(self):
        raise NotImplemented

    @abstractmethod
    def add_establishment(self, establishment: Establishment_domain):
        raise NotImplemented

    @abstractmethod
    def update_establishment(self, establishment: Establishment_domain, establishment_id: str):
        raise NotImplemented

    @abstractmethod
    def delete_establishment(self, establishment_id: str):
        raise NotImplemented

    @abstractmethod
    def get_by_uuid(self, uuid: str):
        raise NotImplemented

    @abstractmethod
    def get_by_category(self, category: str):
        raise NotImplemented

    @abstractmethod
    def get_by_user(self, user_id: str):
        raise NotImplemented

    @abstractmethod
    def update_portrait(self, content: bytes, filename: str, bucket: str, s3_filename: str) -> str:
        raise NotImplemented

    @abstractmethod
    def create_image_for_establishment(self, establishment_id: str, url: str):
        raise NotImplemented


