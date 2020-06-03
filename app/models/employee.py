from pydantic import BaseModel, validator
from pydantic.fields import Field
from validate_docbr import CPF


class EmployeeModel(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    cpf: str

    @validator('cpf')
    def check_cpf(cls, v):
        if not CPF().validate(v):
            raise ValueError(f"CPF {v} inválido")
        return v
