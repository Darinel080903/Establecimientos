from pydantic import BaseModel


class CommentEntity(BaseModel):
    user_id: str
    establishment_id: str
    comment: str
    rating: int
