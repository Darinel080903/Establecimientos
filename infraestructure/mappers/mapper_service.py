from typing import List

from domain.model.category_domain import Category_domain
from domain.model.comment_domain import Comment_domain
from domain.model.establishment_domain import Establishment_domain
from domain.model.service_domain import Service_domain
from infraestructure.schema.models_factory import Comment, Establishment, Service, Category
from infraestructure.web.request.establishment_entity import EstablishmentEntity, ServiceEntity, CategoryEntity
from infraestructure.web.request.establishment_update_entity import EstablishmentUpdateEntity


class Comment_mapper_service:
    @staticmethod
    def db_to_domain(comment: Comment) -> Comment_domain:
        return Comment_domain(
            user_id=comment.user_id,
            establishment_id=comment.establishment_id,
            comment=comment.comment,
            rating=comment.rating
        )

    @staticmethod
    def domain_to_db(comment: Comment_domain) -> Comment:
        return Comment(
            uuid=comment.uuid,
            user_id=comment.user_id,
            establishment_id=comment.establishment_id,
            comment=comment.comment,
            rating=comment.rating
        )


class Establishment_mapper_service:

    @staticmethod
    def db_to_domain(establishment: Establishment) -> Establishment_domain:
        establishment_domain = Establishment_domain(
            name=establishment.name,
            description=establishment.description,
            opening_hours=establishment.opening_hours,
            closing_hours=establishment.closing_hours,
            address=establishment.address,
            days=establishment.days,
            services=Service_mapper_service.db_to_domain(establishment.service),
            category=establishment.category_id,
            user_id=establishment.user_id
        )
        establishment_domain.uuid = establishment.uuid
        return establishment_domain

    @staticmethod
    def domain_to_db(establishment: Establishment_domain) -> Establishment:
        return Establishment(
            uuid=establishment.uuid,
            name=establishment.name,
            description=establishment.description,
            opening_hours=establishment.opening_hours,
            closing_hours=establishment.closing_hours,
            days=establishment.days,
            address=establishment.address,
            category_id=establishment.category,
            user_id=establishment.user_id
        )

    @staticmethod
    def entity_to_domain(establishment_entity: EstablishmentEntity) -> Establishment_domain:
        return Establishment_domain(
            name=establishment_entity.name,
            description=establishment_entity.description,
            opening_hours=establishment_entity.opening_hours,
            closing_hours=establishment_entity.closing_hours,
            days=establishment_entity.days,
            address=establishment_entity.address,
            services=Service_mapper_service.entities_to_domains(establishment_entity.services),
            category=establishment_entity.category,
        )

    @staticmethod
    def entity_to_domain_update(establishment_entity: EstablishmentUpdateEntity) -> Establishment_domain:
        return Establishment_domain(
            name=establishment_entity.name,
            description=establishment_entity.description,
            opening_hours=establishment_entity.opening_hours,
            closing_hours=establishment_entity.closing_hours,
            days=establishment_entity.days,
            address=establishment_entity.address,
            services=[],
            category='',
        )


class Service_mapper_service:
    @staticmethod
    def db_to_domain(services: List[Service]) -> List[Service_domain]:
        return [Service_domain(name=service.name) for service in services]

    @staticmethod
    def domain_to_db(service: Service_domain) -> Service:
        return Service(
            uuid=service.uuid,
            name=service.name,
        )

    @staticmethod
    def entities_to_domains(service_entities: List[ServiceEntity]) -> List[Service_domain]:
        domain = []
        for service_entity in service_entities:
            domain.append(Service_domain(name=service_entity.name))

        print(domain[0].name)
        return domain


class Category_mapper_service:
    @staticmethod
    def db_to_domain(category: Category) -> Category_domain:
        return Category_domain(
            name=category.name,
        )

    @staticmethod
    def domain_to_db(category: Category_domain) -> Category:
        return Category(
            uuid=category.uuid,
            name=category.name,
        )

    @staticmethod
    def entity_to_domain(category_entity: CategoryEntity) -> Category_domain:
        return Category_domain(
            name=category_entity.name,
        )
