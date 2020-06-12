

class AgencyModel:
    account_number = 0
    def __init__(self):
        self.account_number = AgencyModel.account_number
        AgencyModel.account_number += 1
    
