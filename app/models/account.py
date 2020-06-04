from app.models.agency import AgencyModel

class AccountModel:
    def __init__(self):
        self._balance = 0
        self.agency = AgencyModel()
    
    @property
    def balance(self):
        return self._balance
