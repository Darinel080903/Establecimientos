from fastapi import APIRouter, UploadFile, Depends

from application.service.comment_service import Comment_service
from application.service.establishment_service import Establishment_service
from infraestructure.configuration.auth_bear import JWTBearer
from infraestructure.mappers.mapper_service import Establishment_mapper_service
from infraestructure.repository import establishment_repository_impl, category_repository_impl, service_repository_impl, \
    gallery_repository_impl
from infraestructure.repository.comment_repository_impl import Comment_repository_impl
from infraestructure.web.request.comment_entity import CommentEntity
from infraestructure.web.request.establishment_entity import EstablishmentEntity
from infraestructure.web.request.establishment_update_entity import EstablishmentUpdateEntity

controller = APIRouter()
repository = establishment_repository_impl.Establishment_repository_impl()
category_repository = category_repository_impl.Category_repository_impl()
service_repository = service_repository_impl.Service_repository_impl()
gallery_repository = gallery_repository_impl.Gallery_repository_impl()
service = Establishment_service(repository, category_repository, service_repository, gallery_repository)
repository_comments = Comment_repository_impl()
service_comments = Comment_service(repository_comments)

default_route = '/api/v1'


@controller.get(default_route + "/establishment", dependencies=[Depends(JWTBearer())])
def get_establishments():
    establishments = service.get_all()
    return establishments


@controller.get(default_route + "/comments", dependencies=[Depends(JWTBearer())])
def get_comments():
    comments = service_comments.get_all()
    return comments


@controller.post(default_route + "/establishment/create/{user_id}", dependencies=[Depends(JWTBearer())])
def create_establishment(establishment: EstablishmentEntity, user_id: str):
    print(establishment.services.__str__())
    establishment = Establishment_mapper_service.entity_to_domain(establishment)
    establishment_save = service.add_establishment(establishment, user_id)
    return establishment_save


@controller.put(default_route + "/establishment/update/{establishment_id}", dependencies=[Depends(JWTBearer())])
def update_establishment(establishment: EstablishmentUpdateEntity, establishment_id: str):
    establishment = Establishment_mapper_service.entity_to_domain_update(establishment)
    establishment_save = service.update_establishment(establishment, establishment_id)
    return establishment_save


@controller.post(default_route + "/establishment/add/portrait/{establishment_id}", dependencies=[Depends(JWTBearer())])
def post_image(establishment_id: str, file: UploadFile):
    return service.add_portrait_image(file.file.read(), file.filename, establishment_id)


@controller.get(default_route + "/category")
def get_categories():
    categories = service.get_categories()
    return categories


@controller.get(default_route + "/establishment/by/{user_id}", dependencies=[Depends(JWTBearer())])
def get_by_user(user_id: str):
    establishments = service.get_by_user(user_id)
    return establishments


@controller.post(default_route + "/establishment/add/gallery/{establishment_id}", dependencies=[Depends(JWTBearer())])
def post_gallery_images(establishment_id: str, files: list[UploadFile]):
    return service.add_gallery_image(files, establishment_id)


@controller.get(default_route + "/establishment/gallery/{establishment_id}", dependencies=[Depends(JWTBearer())])
def get_gallery(establishment_id: str):
    return service.get_gallery(establishment_id)


@controller.delete(default_route + "/establishment/gallery/{gallery_id}", dependencies=[Depends(JWTBearer())])
def delete_gallery(gallery_id: str):
    return service.delete_gallery(gallery_id)


@controller.get(default_route + "/hour/{establishment_id}")
def get_establishment(establishment_id: str):
    return service.hours_by_uuid(establishment_id)


@controller.get(default_route + "comment/establishment/{establishment_id}", dependencies=[Depends(JWTBearer())])
def get_comment_by_establishment(establishment_id: str):
    return service_comments.get_by_establishment(establishment_id)


@controller.post(default_route + "/comment/create/")
def create_comment(comment: CommentEntity):
    return service_comments.add_comment(comment.user_id, comment.establishment_id, comment.comment, comment.rating)


@controller.get(default_route + "/establishment/{establishment_id}")
def get_establishment(establishment_id: str):
    return service.get_by_uuid(establishment_id)


@controller.get(default_route + '/health')
def health():
    return {"status": "Ok"}
