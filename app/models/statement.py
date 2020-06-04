from typing import List
from datetime import datetime

from pydantic import BaseModel


class StatementModel(BaseModel):
    timestamp: datetime = datetime.now()
    description: str = None
    withdraw: int = None
    deposit: int = None
    balance: int


class StatementModelList(BaseModel):
    statements: List[StatementModel]

    def add(
        self,
        balance: int, 
        description: str = None, 
        withdraw: int = None, 
        deposit: int = None
        ):
        self.statements.append(
            StatementModel(
                description=description,
                withdraw=withdraw,
                deposit=deposit,
                balance=balance
            )
        )        
