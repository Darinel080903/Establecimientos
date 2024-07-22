from abc import ABC

from domain.model.service_domain import Service_domain
from domain.repository.service_respository import Service_repository
from infraestructure.configuration.db import SessionLocal
from infraestructure.mappers.mapper_service import Service_mapper_service


class Service_repository_impl(Service_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def add_service(self, service: list[Service_domain], establishment_id: str):
        print(service.__str__())
        model = [Service_mapper_service.domain_to_db(service) for service in service]
        for service in model:
            service.establishment_id = establishment_id
        print(model.__str__())
        self.db.bulk_save_objects(model)
        self.db.commit()
        return Service_mapper_service.db_to_domain(model)

    def update_service(self, service: Service_domain, service_id: str):
        pass
