from abc import ABC

from domain.model.comment_domain import Comment_domain
from domain.model.dto.response.base_response import Base_response
from domain.repository.comment_repository import Comment_repository
from domain.use_case.comment_use_case import Comment_use_case
from sklearn.linear_model import LinearRegression
import numpy as np


class Comment_service(Comment_use_case, ABC):
    def __init__(self, comment_repository: Comment_repository):
        self.comment_repository = comment_repository

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
        rt = 0
        try:
            rating = self.comment_repository.get_by_establishment(establishment_uuid)
            for rate in rating:
                rt += rate.rating
            rating = rt / len(rating)
            return Base_response(data=rating, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_sentimental_analysis(self, establishment_uuid: str) -> Base_response:
        try:
            sentimental_analysis = self.comment_repository.get_all()
            return Base_response(data=sentimental_analysis, message="Success", code=200)
        except Exception as e:
            return Base_response(data=None, message=str(e), code=500)

    def get_ratings_over_time(self, establishment_id: str, interval: str):
        return self.comment_repository.get_ratings_over_time(establishment_id, interval)

    def predict_future_rating(self, establishment_id: str, interval: str):
        ratings_over_time = self.get_ratings_over_time(establishment_id, interval)
        time_values = np.array([i[0].timestamp() for i in ratings_over_time]).reshape(-1, 1)
        ratings = np.array([i[1] for i in ratings_over_time])
        model = LinearRegression()
        model.fit(time_values, ratings)

        last_timestamp = time_values[-1][0]

        future_time = last_timestamp + 3600 * 24

        if interval == "1H":
            future_time = last_timestamp + 3600 * 2
        elif interval == "1D":
            future_time = last_timestamp + 3600 * 24 * 2

        future_time = np.array([future_time]).reshape(-1, 1)
        predicted_rating = model.predict(future_time)

        return predicted_rating
