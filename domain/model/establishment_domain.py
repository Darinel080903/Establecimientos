from uuid import uuid4

from domain.model.category_domain import Category_domain
from domain.model.service_domain import Service_domain


class Establishment_domain:
    def __init__(self, name: str, description: str, opening_hours: str, closing_hours: str,
                 days: str, services: list[Service_domain], address: str, category, user_id: str = None):
        self._uuid = str(uuid4())
        self._name = name
        self._description = description
        self._opening_hours = opening_hours
        self._closing_hours = closing_hours
        self._days = days
        self._address = address
        self._services = services
        self._category = category
        self._user_id = user_id

    @property
    def uuid(self):
        return self._uuid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def portrait(self):
        return self._portrait

    @portrait.setter
    def portrait(self, value):
        self._portrait = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        self._opening_hours = value

    @property
    def closing_hours(self):
        return self._closing_hours

    @closing_hours.setter
    def closing_hours(self, value):
        self._closing_hours = value

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        if isinstance(value, list):
            self._days = value

    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, value):
        if isinstance(value, list):
            self._services = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, int):
            self._category = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
