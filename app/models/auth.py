

class AuthModel:
    def __init__(self):
        self.user = None
        self._passwd = 'None'
    
    @property
    def passwd(self):
        return self._passwd

    def check_password(self, passwd):
        return self._passwd == passwd
    
