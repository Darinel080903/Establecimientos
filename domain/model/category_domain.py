from uuid import uuid4


class Category_domain:
    def __init__(self, uuid: str, name: str):
        self._uuid = uuid
        self._name = name

    @property
    def uuid(self):
        return self.uuid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @uuid.setter
    def uuid(self, value):
        self._uuid = value
