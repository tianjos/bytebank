from typing import Dict

from app.models.client import ClientModel, ClientModelList
from app.models.account import AccountModel
from app.views.client import ClientView
from app.services.filter_client import FilterClientService


class ClientController:
    def __init__(self):
        self.client_view =  ClientView()
        self.clients = ClientModelList()

    def add_client(self, client_data: Dict[str, str], account: AccountModel):
        self.clients.push(
            ClientModel(name=client_data['name'], cpf=client_data['cpf'], account=account)
        )
    
    def open_account(self, client_data: Dict[str, str]):
        account = AccountModel()
        self.add_client(client_data, account)
    
    def deposit(self, client: ClientModel, value: float):
        client.account.deposit(value)
    
    def transfer(self, from_client, to_client, value):
        from_account = FilterClientService.filter_by_attr('cpf', from_client, self.clients)
        to_account = FilterClientService.filter_by_attr('cpf', to_client, self.clients)
        from_account.account.transfer(to_account, value)

    def withdraw(self, account: ClientModel, value: float, description: str):
        account.withdraw(value, description)




    
