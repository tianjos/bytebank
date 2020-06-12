from typing import Dict

from app.models.client import ClientModel, ClientModelList
from app.models.account import AccountModel
from app.views.client import ClientView
from app.services.index_client import IndexClient


class ClientController:
    def __init__(self):
        self.client_view =  ClientView()
        self.clients = ClientModelList()
        self._index_client = IndexClient()

    def _get_client(self, username: str) -> ClientModel:
        client_position = self._index_client.get(username)
        return self.clients[client_position]

    def add_client(self, client_data: Dict[str, str], account: AccountModel):
        # return self.clients.push(
        #     ClientModel(username=client_data['username'], account=account)
        # )
        client_model = ClientModel(username=client_data['username'], account=account)
        client_model.create_passwd(client_data['passwd'])
        return self.clients.push(client_model)
    
    def open_account(self, client_data: Dict[str, str]):
        account = AccountModel()
        client_index_position = self.add_client(client_data, account)
        self._index_client.add(client_data['username'], client_index_position)

    def deposit(self, client: str, value: float):
        client_model = self._get_client[client]
        client_model.account.deposit(value)
    
    def transfer(self, from_client: str, to_client: str, value: float, description: str = None):
        from_client_model = self._get_client(from_client)
        to_client_model = self._get_client(to_client)
        from_client_model.account.transfer(to_client_model, value, description)

    def withdraw(self, client: str, value: float, description: str = None):
        client_model = self._get_client(client)
        client_model.account.withdraw(value, description)
    
    def show_statements(self, client: str):
        client_model = self._get_client(client)
        client_model.account.show_statements()
    
    def show_balance(self, client: str):
        client_model = self._get_client(client)
        print(client_model.account.balance)
