from app.models.agency import AgencyModel
from app.models.statement import StatementModelList


class AccountModel:
    def __init__(self):
        self._balance = 0
        self.agency = AgencyModel()
        self._statements = StatementModelList()
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, value: int, description: str = None):
        self._balance += value
        self._statements.add(balance=self.balance, description=description, deposit=value)
    
    def withdraw(self, value: int, description: str = None):
        self._balance -= value
        self._statements.add(balance=self.balance, description=description, withdraw=value)
        return value

    def transfer(self, value: int, account: 'AccountModel', description: str = None):
        account.deposit(value, description)
        self.withdraw(value, description)
