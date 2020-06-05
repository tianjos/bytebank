from typing import Dict, List, TypeVar
from pydantic import BaseModel, validator
from pydantic.fields import Field
from validate_docbr import CPF


AccountModelType = TypeVar('Account')


class ClientModel(BaseModel):
    username: str = Field(min_length=2, max_length=20)
    # cpf: str
    account: AccountModelType

    # @validator('cpf')
    # def check_cpf(cls, v):
    #     if not CPF().validate(v):
    #         raise ValueError(f"CPF {v} inválido")
    #     return v

class ClientModelList:

    def __init__(self):
        self.__clients: List[ClientModel] = []
        self.__index = 0
        self.__counter = 1
    
    def __repr__(self) -> str:
        return f'Clients: <{[item for item in self.__clients]}>'

    def __len__(self):
        return len(self.__clients)
    
    def __contains__(self, value: str, attr: str = 'cpf') -> bool:
        return any([True if getattr(client, attr) == value else False for client in self])

    def __getitem__(self, i) -> 'Client':
        return self.__clients[i]
    
    def __delitem__(self, i):
        del self.__clients[i]
        self.__index -= 1
    
    def __iter__(self):
        return iter(self.__clients)

    def __next__(self):
        return next(self.__clients)

    def push(self, client: ClientModel):
        self.__clients.append(client)
        self.__index += 1
        return self.__index - 1
    
    def push_left(self, item):
        self.push(item)
        size = len(self.__clients)
        for index in range((size - 1), 0, -1):
            self.__clients[index], self.__clients[index - 1] = self.__clients[index - 1], self.__clients[index]
        
    def pop(self) -> 'Client':
        item = self.__clients[len(self.__clients) -1]
        del self.__clients[len(self.__clients) -1]
        return item
    
    def pop_left(self) -> 'Client':
        item = self.__clients[0]
        del self.__clients[0]
        return item
