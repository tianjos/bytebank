from app.controllers.client import ClientController

client_controller = ClientController()
client_controller.add_client({'name': 'foo', 'cpf':'bar'})
client_controller.client_view.render(client_controller.clients)
