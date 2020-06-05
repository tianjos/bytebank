from app.controllers.client import ClientController

client_controller = ClientController()
client_controller.open_account({'username': 'foo'})
client_controller.open_account({'username': 'bar'})
client_controller.deposit('foo', 'bar', 100)
client_controller.client_view.render(client_controller.clients)


