from abc import ABC

from domain.repository.gallery_repository import Gallery_repository
from infraestructure.configuration.db import SessionLocal
from infraestructure.schema.models_factory import Gallery


class Gallery_repository_impl(Gallery_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def get_by_establishment(self, establishment_id: str):
        return self.db.query(Gallery).filter(Gallery.establishment_id == establishment_id).all()

    def upload_image(self, content: bytes, filename: str, bucket: str, s3_filename: str) -> str:
        pass

    def add_gallery(self, gallery: list[str], establishment_id: str):
        model = [Gallery(url=image, establishment_id=establishment_id) for image in gallery]
        self.db.bulk_save_objects(model)
        self.db.commit()

    def delete_gallery(self, gallery_id: str):
        gallery_db = self.db.query(Gallery).filter(Gallery.uuid == gallery_id).first()
        self.db.delete(gallery_db)
        self.db.commit()

