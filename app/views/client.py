class ClientView:
    
    def render(self, clients):
        for client in clients:
            print(f"Cliente: {client.name}, CPF: {client.cpf}")
            # print(client.dict())
