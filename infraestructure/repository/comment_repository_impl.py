from abc import ABC

from domain.model.comment_domain import Comment_domain
from domain.repository.comment_repository import Comment_repository
from infraestructure.configuration.db import SessionLocal
from infraestructure.mappers.mapper_service import Comment_mapper_service
from infraestructure.schema.models_factory import Comment


class Comment_repository_impl(Comment_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self) -> list[Comment_domain]:
        comments = self.db.query(Comment).all()
        self.db.close()
        return [Comment_mapper_service.db_to_domain(comment) for comment in comments]

    def add_comment(self, comment: Comment) -> Comment_domain:
        self.db.add(comment)
        self.db.commit()
        self.db.refresh(comment)
        return Comment_mapper_service.db_to_domain(comment)

    def delete_comment(self, comment_id: str):
        comment_db = self.db.query(Comment).filter(Comment.uuid == comment_id).first()
        self.db.delete(comment_db)
        self.db.commit()

    def get_by_establishment(self, uuid: str) -> list[Comment_domain]:
        filtered_comments = self.db.query(Comment).filter(Comment.establishment_id == uuid).all()
        return [Comment_mapper_service.db_to_domain(comment) for comment in filtered_comments]

    def get_by_user(self, user_id: str) -> list[Comment_domain]:
        filtered_comments = self.db.query(Comment).filter(Comment.user_id == user_id).all()
        return [Comment_mapper_service.db_to_domain(comment) for comment in filtered_comments]