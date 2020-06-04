from typing import List
from datetime import datetime

from pydantic import BaseModel


class StatementModel(BaseModel):
    timestamp: datetime = datetime.now()
    description: str = None
    withdrawal: int
    deposit: int
    balance: int


class StatementModelList(BaseModel):
    statements: List[StatementModel]
