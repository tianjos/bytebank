import re
from datetime import datetime, timedelta
from pydantic import BaseModel, validator 


PASSWD_REGEX = re.compile('\w+\W+')
EXPIRES_DAYS = 90


class PasswordModel(BaseModel):
    passwd: str
    created: datetime = datetime.utcnow()
    expires: datetime = created + timedelta(days=EXPIRES_DAYS)

    @validator('passwd')
    def validated_passwd(cls, v):
        match = PASSWD_REGEX.match(v)
        if not match or len(v) < 8:
            raise ValueError(f'password does not match criteria')
    
    def check_passwd(self, password: str) -> bool:
        return self.passwd == password
    

