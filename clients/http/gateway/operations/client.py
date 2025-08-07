from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client  # Импортируем builder


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

class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationDict]

class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationDict

# Operation summary example response structure:
# {
#   "summary": {
#     "spentAmount": 0,
#     "receivedAmount": 0,
#     "cashbackAmount": 0
#   }
# }

class OperationSummaryDict(TypedDict):
    """
    Описание структуры сводки по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа получения сводки по операциям.
    """
    summary: OperationSummaryDict

# Example structure for operation receipt:
# {
#   "receipt": {
#     "url": "https://example.com/",
#     "document": "string"
#   }
# }

class ReceiptDict(TypedDict):
    """
    Описание структуры чека операции.
    """
    url: str
    document: str

class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры ответа получения чека операции.
    """
    receipt: ReceiptDict


# Example structure for making an operation response:
# {
#   "status": "FAILED",
#   "amount": 0,
#   "cardId": "string",
#   "accountId": "string"
# }

class MakeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа создания операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str

class GetOperationsQueryDict(TypedDict):
    accountId: str

class MakeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    category: str



class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, accountId: str) -> Response:
        """
        Получить операции по номеру счета.

        :param accountId: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=GetOperationsQueryDict(accountId=accountId))

    def get_operations_summary_api(self, accountId: str) -> Response:
        """
        Получить статистику по операциям для определенного счета.

        :param accountId: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operations-summary", params=GetOperationsQueryDict(accountId=accountId))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получить данные операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.
        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.
        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.
        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получить список операций по счету.

        :param account_id: Идентификатор счета.
        :return: Список операций.
        """
        response = self.get_operations_api(account_id)
        response.raise_for_status()
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получить сводку по операциям для определенного счета.

        :param account_id: Идентификатор счета.
        :return: Сводка по операциям.
        """
        response = self.get_operations_summary_api(account_id)
        response.raise_for_status()
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получить данные операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Данные операции.
        """
        response = self.get_operation_api(operation_id)
        response.raise_for_status()
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Чек операции в виде строки.
        """
        response = self.get_operation_receipt_api(operation_id)
        response.raise_for_status()
        return response.text


    def make_fee_operation(self, request: MakeOperationRequestDict) -> MakeOperationResponseDict:
        """
        Создать операцию комиссии.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_fee_operation_api(request)
        response.raise_for_status()
        return response.json()

    def make_top_up_operation(self, request: MakeOperationRequestDict) -> MakeOperationResponseDict:
        """
        Создать операцию пополнения.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_top_up_operation_api(request)
        response.raise_for_status()
        return response.json()

    def make_cashback_operation(self, request: MakeOperationRequestDict) -> MakeOperationResponseDict:
        """
        Создать операцию кэшбэка.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_cashback_operation_api(request)
        response.raise_for_status()
        return response.json()

    def make_transfer_operation(self, request: MakeOperationRequestDict) -> MakeOperationResponseDict:
        """
        Создать операцию перевода.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_transfer_operation_api(request)
        response.raise_for_status()
        return response.json()

    def make_purchase_operation(self, request: MakePurchaseOperationRequestDict) -> MakeOperationResponseDict:
        """
        Создать операцию покупки.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_purchase_operation_api(request)
        response.raise_for_status()
        return response.json()

    def make_bill_payment_operation(self, request: MakeOperationRequestDict) -> MakeOperationResponseDict:
        """
        Создать операцию оплаты по счету.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_bill_payment_operation_api(request)
        response.raise_for_status()
        return response.json()

    def make_cash_withdrawal_operation(self, request: MakeOperationRequestDict) -> MakeOperationResponseDict:
        """
        Создать операцию снятия наличных денег.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_cash_withdrawal_operation_api(request)
        response.raise_for_status()
        return response.json()

# Добавляем builder для OperationsGatewayHTTPClient
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Создает и возвращает экземпляр OperationsGatewayHTTPClient.

    :return: Экземпляр OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
