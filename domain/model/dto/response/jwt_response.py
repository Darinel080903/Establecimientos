class Jwt_response:
    def __init__(self, token: str, email: str):
        self.token = token
        self.email = email

    def get_token(self):
        return self.token

    def get_email(self):
        return self.email

    def set_token(self, token):
        self.token = token

    def set_email(self, email):
        self.email = email
