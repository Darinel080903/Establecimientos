from pydantic import BaseModel


class EstablishmentUpdateEntity(BaseModel):
    name: str
    description: str
    opening_hours: str
    closing_hours: str
    days: str
    address: str
