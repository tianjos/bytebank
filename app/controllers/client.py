from typing import Dict

from app.models.client import ClientModel, ClientModelList
from app.models.account import AccountModel
from app.views.client import ClientView
from app.services.filter_client import FilterClientService
from app.services.index_client import IndexClient


class ClientController:
    def __init__(self):
        self.client_view =  ClientView()
        self.clients = ClientModelList()
        self._index_client = IndexClient()

    def add_client(self, client_data: Dict[str, str], account: AccountModel):
        self.clients.push(
            ClientModel(name=client_data['name'], account=account)
        )
    
    def open_account(self, client_data: Dict[str, str]):
        account = AccountModel()
        self.add_client(client_data, account)
    
    def deposit(self, client: ClientModel, value: float):
        client.account.deposit(value)
    
    # def transfer(self, from_client_id, to_client_id, value):
    #     from_client = FilterClientService.filter_by_attr('username', from_client_id, self.clients)
    #     to_client = FilterClientService.filter_by_attr('username', to_client_id, self.clients)
    #     from_client.account.transfer(to_client, value)

    def transfer(self, from_client: ClientModel, to_client: ClientModel, value: float, description: str = None):
        from_client.account.transfer(to_client, value, description)

    def withdraw(self, client: ClientModel, value: float, description: str):
        client.account.withdraw(value, description)
