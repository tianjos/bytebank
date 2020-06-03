from app.models.client import ClientModel, ClientModelList
from app.views.client import ClientView

class ClientController:
    def __init__(self):
        # self.client_model = ClientModel(name=name, cpf=cpf)
        self.client_view =  ClientView()
        self.clients = ClientModelList()

    def add_client(self, data: dict):
        self.clients.append(
            ClientModel(**data)
        )
    

    
