from abc import ABC, abstractmethod

from domain.repository.comment_repository import Comment_repository


class Comment_use_case(ABC):
    @abstractmethod
    def __init__(self, comment_repository: Comment_repository):
        self.comment_repository = comment_repository

    @abstractmethod
    def get_all(self):
        raise NotImplemented

    @abstractmethod
    def add_comment(self, user_id: str, establishment_id: str, comment: str, rating: int):
        raise NotImplemented

    @abstractmethod
    def delete_comment(self, comment_id: str):
        raise NotImplemented

    @abstractmethod
    def get_by_establishment(self, uuid: str):
        raise NotImplemented

    @abstractmethod
    def get_by_user(self, user_id: str):
        raise NotImplemented

    @abstractmethod
    def get_rating_establishment(self, establishment_uuid: str):
        raise NotImplemented

    @abstractmethod
    def get_sentimental_analysis(self, establishment_uuid: str):
        raise NotImplemented


