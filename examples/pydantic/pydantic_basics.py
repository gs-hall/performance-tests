from pydantic import BaseModel


class AccountSchema(BaseModel):
    id: str
    type: str
    status: str
    balance: float

account_default_model = AccountSchema(
    id="account-id",
    type="CREDIT_CARD",
    status="ACTIVE",
    balance=100.57,
)
print('Account default model:', account_default_model)

account_dict = {
    "id": "account-id",
    "type": "CREDIT_CARD",
    "status": "ACTIVE",
    "balance": 777.11,
}
account_dict_model = AccountSchema(**account_dict)
print('Account dict model:', account_dict_model)
