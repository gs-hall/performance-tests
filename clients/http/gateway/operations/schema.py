from datetime import datetime
from enum import StrEnum
from tools.fakers import fake
from pydantic import BaseModel, Field, ConfigDict, HttpUrl, UUID4

class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"

# Operations example response structure:
# {
#   "operations": [
#     {
#       "id": "string",
#       "type": "FEE",
#       "status": "FAILED",
#       "amount": 0,
#       "cardId": "string",
#       "category": "string",
#       "createdAt": "2025-08-07T17:27:30.777Z",
#       "accountId": "string"
#     }
#   ]
# }

class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: UUID4
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: UUID4 = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: UUID4 = Field(alias="accountId")

class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций по счету.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    account_id: UUID4 = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationSchema]

class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationSchema

# Operation summary example response structure:
# {
#   "summary": {
#     "spentAmount": 0,
#     "receivedAmount": 0,
#     "cashbackAmount": 0
#   }
# }

class OperationSummarySchema(BaseModel):
    """
    Описание структуры сводки по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения сводки по операциям.
    """
    summary: OperationSummarySchema

# Example structure for operation receipt:
# {
#   "receipt": {
#     "url": "https://example.com/",
#     "document": "string"
#   }
# }

class ReceiptSchema(BaseModel):
    """
    Описание структуры чека операции.
    """
    url: HttpUrl
    document: str

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека операции.
    """
    receipt: ReceiptSchema

# Example structure for making an operation response:
# {
#   "status": "FAILED",
#   "amount": 0,
#   "cardId": "string",
#   "accountId": "string"
# }

# Fee
class MakeFeeOperationRequestSchema(BaseModel):
    """
    Описание структуры запроса создания операции комиссии.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции комиссии.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    operation: OperationSchema

# TopUp
class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Описание структуры запроса создания операции пополнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции пополнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    operation: OperationSchema

# Cashback
class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Описание структуры запроса создания операции кэшбэка.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    operation: OperationSchema

# Transfer
class MakeTransferOperationRequestSchema(BaseModel):
    """
    Описание структуры запроса создания операции перевода.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции перевода.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    operation: OperationSchema

# Purchase
class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Описание структуры запроса создания операции покупки.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=lambda: fake.category())

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции покупки.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    operation: OperationSchema

# Bill Payment
class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Описание структуры запроса создания операции оплаты счета.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции оплаты счета.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    operation: OperationSchema

# Cash Withdrawal
class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Описание структуры запроса создания операции снятия наличных.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda: fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции снятия наличных.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
    operation: OperationSchema

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения сводки по операциям.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    account_id: UUID4 = Field(alias="accountId")
