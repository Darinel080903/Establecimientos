class Base_response:
    def __init__(self, message: str, code: int, data: object):
        self.message = message
        self.code = code
        self.data = data

    def to_dict(self):
        return {
            'message': self.message,
            'code': self.code,
            'data': self.data
        }