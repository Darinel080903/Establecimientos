import uuid


class Comment_domain:
    def __init__(self, user_id: str, establishment_id: str, comment: str, rating: int):
        self.uuid = str(uuid.uuid4())
        self._user_id = user_id
        self._establishment_id = establishment_id
        self._comment = comment
        self._rating = rating

    @property
    def user_id(self):
        return self._user_id

    @property
    def establishment_id(self):
        return self._establishment_id

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
