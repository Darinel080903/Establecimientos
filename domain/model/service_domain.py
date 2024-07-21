from uuid import uuid4


class Service_domain:
    def __init__(self, name: str):
        self._uuid = str(uuid4())
        self._name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
