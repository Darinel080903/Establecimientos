from fastapi import APIRouter, UploadFile

from application.service.comment_service import Comment_service
from application.service.establishment_service import Establishment_service
from infraestructure.mappers.mapper_service import Establishment_mapper_service
from infraestructure.repository import establishment_repository_impl, category_repository_impl, service_repository_impl
from infraestructure.repository.comment_repository_impl import Comment_repository_impl
from infraestructure.web.request.establishment_entity import EstablishmentEntity

controller = APIRouter()
repository = establishment_repository_impl.Establishment_repository_impl()
category_repository = category_repository_impl.Category_repository_impl()
service_repository = service_repository_impl.Service_repository_impl()
service = Establishment_service(repository, category_repository, service_repository)
repository_comments = Comment_repository_impl()
service_comments = Comment_service(repository_comments)

default_route = '/api/v1'


@controller.get(default_route + "/establishment")
def get_establishments():
    establishments = service.get_all()
    return establishments


@controller.get(default_route + "/comments")
def get_comments():
    comments = service_comments.get_all()
    return comments


@controller.post(default_route + "/establishment/create/{user_id}")
def create_establishment(establishment: EstablishmentEntity, user_id: str):
    print(establishment.services.__str__())
    establishment = Establishment_mapper_service.entity_to_domain(establishment)
    establishment_save = service.add_establishment(establishment, user_id)
    return establishment_save


@controller.post(default_route + "/establishment/add/portrait/{establishment_id}")
def post_image(establishment_id: str, file: UploadFile):
    return service.add_portrait_image(file.file.read(), file.filename, establishment_id)


@controller.get(default_route + "/category")
def get_categories():
    categories = service.get_categories()
    return categories


@controller.get(default_route + '/health')
def health():
    return {"status": "Ok"}
