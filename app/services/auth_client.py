from functools import wraps
from app.models.client import ClientModel


class AuthService:

    def __init__(self):
        self._authenticated_users = set()
    
    def login(self, client: ClientModel, passwd):
        if client.passwd.check_passwd(passwd):
            self._authenticated_users.add(client.username)
        else:
            return 'Senha inválida' 

    def logout(self, username: str):
        self._authenticated_users.discard(username)
        
    def is_logged_in(self, username) -> bool:
        return username in self._authenticated_users
