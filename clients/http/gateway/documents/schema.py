from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict, HttpUrl

# Get tariff document response example
# {
#   "tariff": {
#     "url": "https://example.com/",
#     "document": "string"
#   }
# }

class TariffDocumentSchema(BaseModel):
    """
    Описание структуры документа тарифа.
    """
    url: HttpUrl
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа тарифа.
    """
    tariff: TariffDocumentSchema

# Get contract document response example
# {
#   "contract": {
#     "url": "https://example.com/",
#     "document": "string"
#   }
# }

class ContractDocumentSchema(BaseModel):
    """
    Описание структуры документа контракта.
    """
    url: HttpUrl
    document: str

class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа получения документа контракта.
    """
    contract: ContractDocumentSchema