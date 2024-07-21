from abc import ABC, abstractmethod

from domain.model.comment_domain import Comment_domain


class Comment_repository(ABC):
    @abstractmethod
    def get_all(self) -> list[Comment_domain]:
        raise NotImplemented

    @abstractmethod
    def add_comment(self, comment: Comment_domain) -> Comment_domain:
        raise NotImplemented

    @abstractmethod
    def delete_comment(self, comment_id: str):
        raise NotImplemented

    @abstractmethod
    def get_by_establishment(self, uuid: str) -> list[Comment_domain]:
        raise NotImplemented

    @abstractmethod
    def get_by_user(self, user_id: str) -> list[Comment_domain]:
        raise NotImplemented
