from abc import ABC

from domain.model.service_domain import Service_domain


class Service_repository(ABC):
    def add_service(self, service: list[Service_domain]):
        raise NotImplemented

    def update_service(self, service: Service_domain, service_id: str):
        raise NotImplemented
