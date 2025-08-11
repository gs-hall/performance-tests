from httpx import Response, QueryParams
from locust.env import Environment  # Импорт окружения Locust
from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationResponseSchema,
    GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
    GetOperationsSummaryQuerySchema,
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, account_id: str) -> Response:
        """
        Получить операции по номеру счета.

        :param accountId: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            "/api/v1/operations",
            params=GetOperationsQuerySchema(account_id=account_id),
            extensions=HTTPClientExtensions(route="/api/v1/operations")
            )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получить статистику по операциям для определенного счета.

        :param accountId: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"/api/v1/operations/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route="/api/v1/operations/operations-summary")
            )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"/api/v1/operations/operation-receipt/{operation_id}",
            extensions=HTTPClientExtensions(route="/api/v1/operations/operation-receipt/{operation_id}")
            )

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получить данные операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f"/api/v1/operations/{operation_id}",
            extensions=HTTPClientExtensions(route="/api/v1/operations/{operation_id}")
            )

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создание операции кэшбэка.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> MakePurchaseOperationResponseSchema:
        """
        Создание операции покупки.
        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> MakeBillPaymentOperationResponseSchema:
        """
        Создание операции оплаты по счету.
        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создание операции снятия наличных денег.
        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получить список операций по счету.

        :param account_id: Идентификатор счета.
        :return: Список операций.
        """
        response = self.get_operations_api(account_id)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получить сводку по операциям для определенного счета.

        :param account_id: Идентификатор счета.
        :return: Сводка по операциям.
        """
        response = self.get_operations_summary_api(account_id)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получить данные операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Данные операции.
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получить чек по операции.

        :param operation_id: Идентификатор операции.
        :return: Чек операции в виде строки.
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)


    def make_fee_operation(self, request: MakeFeeOperationRequestSchema) -> MakeFeeOperationResponseSchema:
        """
        Создать операцию комиссии.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """

        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, request: MakeTopUpOperationRequestSchema) -> MakeTopUpOperationResponseSchema:
        """
        Создать операцию пополнения.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """

        response = self.make_top_up_operation_api(request)
        print('Make top up operation response:', response.status_code, response.text)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, request: MakeCashbackOperationRequestSchema) -> MakeCashbackOperationResponseSchema:
        """
        Создать операцию кэшбэка.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, request: MakeTransferOperationRequestSchema) -> MakeTransferOperationResponseSchema:
        """
        Создать операцию перевода.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, request: MakePurchaseOperationRequestSchema) -> MakePurchaseOperationResponseSchema:
        """
        Создать операцию покупки.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, request: MakeBillPaymentOperationRequestSchema) -> MakeBillPaymentOperationResponseSchema:
        """
        Создать операцию оплаты по счету.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, request: MakeCashWithdrawalOperationRequestSchema) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создать операцию снятия наличных денег.

        :param request: Словарь с данными операции.
        :return: Данные созданной операции.
        """
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)

# Добавляем builder для OperationsGatewayHTTPClient
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Создает и возвращает экземпляр OperationsGatewayHTTPClient.

    :return: Экземпляр OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())

# Новый билдер для нагрузочного тестирования
def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient, адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayHTTPClient с хуками сбора метрик.
    """
    # Возвращаем клиент с хуками для сбора метрик
    return OperationsGatewayHTTPClient(
        client=build_gateway_locust_http_client(environment)
    )