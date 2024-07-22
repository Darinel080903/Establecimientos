from pydantic import BaseModel
from typing import List


class ServiceEntity(BaseModel):
    name: str


class CategoryEntity(BaseModel):
    name: str


class EstablishmentEntity(BaseModel):
    name: str
    description: str
    opening_hours: str
    closing_hours: str
    days: str
    category: str
    services: List[ServiceEntity]
    address: str
