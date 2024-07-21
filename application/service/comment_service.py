from abc import ABC

from domain.model.comment_domain import Comment_domain
from domain.model.dto.response.base_response import Base_response
from domain.repository.comment_repository import Comment_repository
from domain.use_case.comment_use_case import Comment_use_case


class Comment_service(Comment_use_case, ABC):
    def __init__(self, comment_repository: Comment_repository):
        self.comment_repository = comment_repository
        self.rt = 0

    def get_all(self) -> Base_response:
        try:
            comments = self.comment_repository.get_all()
            return Base_response(data=comments, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def add_comment(self, user_id: str, establishment_id: str, comment: str, rating: int) -> Base_response:
        try:
            comment = Comment_domain(user_id=user_id, establishment_id=establishment_id, comment=comment, rating=rating)
            comment = self.comment_repository.add_comment(comment)
            return Base_response(data=comment, message="Success", code=201)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def delete_comment(self, comment_id: str) -> Base_response:
        try:
            self.comment_repository.delete_comment(comment_id)
            return Base_response(data=None, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_establishment(self, uuid: str) -> Base_response:
        try:
            comments = self.comment_repository.get_by_establishment(uuid)
            return Base_response(data=comments, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_by_user(self, user_id: str) -> Base_response:
        try:
            comments = self.comment_repository.get_by_user(user_id)
            return Base_response(data=comments, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_rating_establishment(self, establishment_uuid: str) -> Base_response:
        try:
            rating = self.comment_repository.get_all()
            for rate in rating:
                self.rt += rate.rating
            rating = self.rt / len(rating)
            return Base_response(data=rating, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_sentimental_analysis(self, establishment_uuid: str) -> Base_response:
        try:
            sentimental_analysis = self.comment_repository.get_all()
            return Base_response(data=sentimental_analysis, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

