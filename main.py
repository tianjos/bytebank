from app.controllers.client import ClientController


client_controller = ClientController()
client_controller.open_account({'username': 'foo', 'passwd': 'AbCd00.-'})
client_controller.open_account({'username': 'bar', 'passwd': 'AbCd00.-'})
client_controller.login('foo', 'AbCd00.-')
client_controller.transfer('foo', 'bar', 100)
client_controller.show_statements('foo')
client_controller.show_balance('foo')
client_controller.client_view.render(client_controller.clients)


