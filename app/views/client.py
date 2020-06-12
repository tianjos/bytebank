

class ClientView:
    
    def render(self, clients):
        for client in clients:
            print(f"Client: {client.username}, Account Number: {client.account.agency.account_number}, balance: {client.account.balance}")
