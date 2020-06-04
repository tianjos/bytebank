from app.models.agency import AgencyModel

class AccountModel:
    def __init__(self):
        self._balance = 0
        self.agency = AgencyModel()
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, value: int):
        self._balance += value
    
    def withdraw(self, value: int):
        self._balance -= value
        return value

    def transfer(self, value: int, account: 'AccountModel'):
        account.deposit(value)
        self._balance -= value
