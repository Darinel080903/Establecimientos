from abc import ABC

from sqlalchemy import func

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

    def add_comment(self, comment: Comment_domain) -> Comment_domain:
        model = Comment_mapper_service.domain_to_db(comment)
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return Comment_mapper_service.db_to_domain(model)

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

    def get_ratings_over_time(self, establishment_id: str, interval: str):
        return (
            self.db.query(
                func.date_trunc(interval, Comment.timestamp).label('time'),
                func.avg(Comment.rating).label('average_rating')
            )
            .filter(Comment.establishment_id == establishment_id)
            .group_by('time')
            .order_by('time')
            .all()
        )
