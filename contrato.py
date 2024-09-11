# Utilizado para validação dos dados
from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Zap com Gemini"
    produto2 = "Zap com GPT"
    produto3 = "Zap com Llama"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: str

#    @validate_call('produto')
#    def categoria_deve_estar_no_enum(cls, v):
#        return v