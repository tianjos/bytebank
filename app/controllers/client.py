from typing import Dict

from app.models.client import ClientModel, ClientModelList
from app.models.account import AccountModel
from app.views.client import ClientView


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
    
    def deposit(self, from_account: ClientModel, to_account: ClientModel, value: int, description: str):
        from_account.transfer(to_account, value, description)

    def withdraw(self, account: ClientModel, value: int, description: str):
        account.withdraw(value, description)
        



    
