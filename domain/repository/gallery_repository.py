from abc import ABC, abstractmethod


class Gallery_repository(ABC):
    @abstractmethod
    def get_by_establishment(self, establishment_id: str):
        raise NotImplemented

    @abstractmethod
    def upload_image(self, content: bytes, filename: str, bucket: str, s3_filename: str) -> str:
        raise NotImplemented

    def add_gallery(self, gallery: list[str], establishment_id: str):
        raise NotImplemented

    @abstractmethod
    def delete_gallery(self, gallery_id: str):
        raise NotImplemented
