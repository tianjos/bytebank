class ClientView:
    
    def render(self, clients):
        for client in clients:
            print(f"Client: {client.name}, CPF: {client.cpf}, Account Number: {client.account.agency.account_number}")
