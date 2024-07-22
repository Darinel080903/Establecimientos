from abc import ABC
from typing import List

from sqlalchemy.orm import joinedload

from domain.model.establishment_domain import Establishment_domain
from domain.repository.establishment_repository import Establishment_repository
from infraestructure.configuration.db import SessionLocal
from infraestructure.mappers.mapper_service import Establishment_mapper_service, Service_mapper_service, \
    Category_mapper_service
from infraestructure.schema.models_factory import Establishment, Category
from infraestructure.schema.models_factory import Service

import boto3


class Establishment_repository_impl(Establishment_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self):
        return self.db.query(Establishment).options(
            joinedload(Establishment.service).load_only(Service.uuid, Service.name),
            joinedload(Establishment.category)).all()

    def add_establishment(self, establishment: Establishment_domain):
        print(establishment.user_id)
        db_model = Establishment_mapper_service.domain_to_db(establishment)
        print(db_model.user_id)
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return Establishment_mapper_service.db_to_domain(db_model)

    def update_establishment(self, establishment: Establishment, establishment_id: str):
        establishment_db = self.db.query(Establishment).filter(Establishment.uuid == establishment_id).first()
        establishment_db.name = establishment.name
        establishment_db.description = establishment.description
        establishment_db.opening_hours = establishment.opening_hours
        establishment_db.closing_hours = establishment.closing_hours
        establishment_db.days = establishment.days
        establishment_db.address = establishment.address
        self.db.commit()
        self.db.refresh(establishment_db)
        return establishment_db

    def delete_establishment(self, establishment_id: str):
        establishment_db = self.db.query(Establishment).filter(Establishment.uuid == establishment_id).first()
        self.db.delete(establishment_db)
        self.db.commit()

    def get_by_uuid(self, uuid: str):
        return self.db.query(Establishment).filter(Establishment.uuid == uuid).first()

    def get_by_category(self, category: str):
        return self.db.query(Establishment).filter(Establishment.category == category).all()

    def get_by_user(self, user_id: str):
        return self.db.query(Establishment).options(joinedload(Establishment.service).load_only(Service.name, Service.uuid), joinedload(Establishment.category)).filter(Establishment.user_id == user_id).all()

    def update_portrait(self, content: bytes, filename: str, bucket: str, s3_filename: str) -> str:
        s3 = boto3.client('s3')
        file_extension = filename.rsplit('.', 1)[1].lower()
        content_type = 'image/jpeg' if file_extension in ['jpg', 'jpeg'] else 'image/png'
        s3.put_object(Bucket=bucket, Key=s3_filename, Body=content, ACL='public-read', ContentType=content_type)
        return f"https://{bucket}.s3.amazonaws.com/{s3_filename}"

    def create_image_for_establishment(self, establishment_id: str, url: str):
        model = self.db.query(Establishment).filter(Establishment.uuid == establishment_id).first()
        model.portrait = url
        self.db.commit()
        self.db.refresh(model)
        self.db.close()
