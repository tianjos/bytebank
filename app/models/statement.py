from typing import List
from datetime import datetime

from pydantic import BaseModel


class StatementModel(BaseModel):
    timestamp: datetime = datetime.now()
    description: str = None
    withdraw: float = None
    deposit: float = None
    balance: float


class StatementModelList(BaseModel):
    statements: List[StatementModel] = []

    def add(
        self,
        balance: float, 
        description: str = None, 
        withdraw: float = None, 
        deposit: float = None
        ):
        self.statements.append(
            StatementModel(
                description=description,
                withdraw=withdraw,
                deposit=deposit,
                balance=balance
            )
        )        
