from grpc import Channel
from locust.env import Environment  # Импорт окружения Locust
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)

from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake

class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет высокоуровневые методы для работы с операциями.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)
        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetOperation через gRPC.

        :param request: gRPC-запрос с данными для получения операции.
        :return: Ответ от сервиса с информацией об операции.
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.

        :param request: gRPC-запрос с данными для получения квитанции по операции.
        :return: Ответ от сервиса с информацией о квитанции.
        """
        return self.stub.GetOperationReceipt(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.

        :param request: gRPC-запрос с данными для пополнения счёта.
        :return: Ответ от сервиса с информацией о выполненной операции пополнения.
        """
        return self.stub.MakeTopUpOperation(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetOperations через gRPC.

        :param request: gRPC-запрос с данными для получения списка операций.
        :return: Ответ от сервиса с информацией о списке операций.
        """
        return self.stub.GetOperations(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.

        :param request: gRPC-запрос с данными для выполнения операции перевода.
        :return: Ответ от сервиса с информацией о выполненной операции перевода.
        """
        return self.stub.MakeTransferOperation(request)

    def get_operations_summary_api(self, query: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.

        :param request: gRPC-запрос с данными для получения сводки по операциям.
        :return: Ответ от сервиса с информацией о сводке по операциям.
        """
        return self.stub.GetOperationsSummary(query)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.

        :param request: gRPC-запрос с данными для выполнения операции оплаты счета.
        :return: Ответ от сервиса с информацией о выполненной операции оплаты счета.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashWithdrawalOperation через gRPC.

        :param request: gRPC-запрос с данными для выполнения операции снятия наличных.
        :return: Ответ от сервиса с информацией о выполненной операции снятия наличных.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.

        :param request: gRPC-запрос с данными для выполнения операции начисления кэшбэка.
        :return: Ответ от сервиса с информацией о выполненной операции начисления кэшбэка.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.

        :param request: gRPC-запрос с данными для выполнения операции начисления комиссии.
        :return: Ответ от сервиса с информацией о выполненной операции начисления комиссии.
        """
        return self.stub.MakeFeeOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.

        :param request: gRPC-запрос с данными для выполнения операции покупки.
        :return: Ответ от сервиса с информацией о выполненной операции покупки.
        """
        return self.stub.MakePurchaseOperation(request)



    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Получение квитанции по операции по её operation_id.

        :param operation_id: Идентификатор операции, для которой требуется квитанция.
        :return: Ответ с информацией о квитанции по операции.
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Получение списка операций для указанного account_id.

        :param account_id: Идентификатор счёта, для которого требуется получить список операций.
        :return: Ответ с информацией о списке операций.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Получение информации об операции по её operation_id.

        :param operation_id: Идентификатор операции, для которой требуется получить информацию.
        :return: Ответ с информацией об операции.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Получение сводки по операциям для указанного account_id.

        :param account_id: Идентификатор счёта, для которого требуется получить сводку по операциям.
        :return: Ответ с информацией о сводке по операциям.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """
        Выполнение операции пополнения счёта для указанного card_id и account_id.

        :param card_id: Идентификатор карты, с которой выполняется перевод.
        :param account_id: Идентификатор счёта, на который выполняется пополнение.
        :return: Ответ с информацией о выполненной операции пополнения.
        """
        request = MakeTopUpOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),  # Генерация случайной суммы
            status=fake.proto_enum(OperationStatus)  # Статус операции
        )
        return self.make_top_up_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """
        Выполнение операции перевода средств.

        :param card_id: Идентификатор карты, с которой выполняется перевод.
        :param account_id: Идентификатор счёта, на который выполняется перевод.
        :return: Ответ с информацией о выполненной операции перевода.
        """
        request = MakeTransferOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),  # Генерация случайной суммы
            status=fake.proto_enum(OperationStatus)  # Статус операции
        )
        return self.make_transfer_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """
        Выполнение операции оплаты счета.

        :param card_id: Идентификатор карты, с которой выполняется оплата.
        :param account_id: Идентификатор счёта, с которого выполняется оплата.
        :return: Ответ с информацией о выполненной операции оплаты счета.
        """
        request = MakeBillPaymentOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)  # Статус операции
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Выполнение операции снятия наличных.

        :param card_id: Идентификатор карты, с которой выполняется снятие наличных.
        :param account_id: Идентификатор счёта, с которого выполняется снятие наличных.
        :return: Ответ с информацией о выполненной операции снятия наличных.
        """
        request = MakeCashWithdrawalOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),  # Генерация случайной суммы
            status=fake.proto_enum(OperationStatus)  # Статус операции
        )
        return self.make_cash_withdrawal_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """
        Выполнение операции начисления кэшбэка.

        :param card_id: Идентификатор карты, для которой выполняется начисление кэшбэка.
        :param account_id: Идентификатор счёта, на который начисляется кэшбэк.
        :return: Ответ с информацией о выполненной операции начисления кэшбэка.
        """
        request = MakeCashbackOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),  # Генерация случайной суммы
            status=fake.proto_enum(OperationStatus)  # Статус операции
        )
        return self.make_cashback_operation_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
        Выполнение операции начисления комиссии.

        :param card_id: Идентификатор карты, для которой выполняется начисление комиссии.
        :param account_id: Идентификатор счёта, на который начисляется комиссия.
        :return: Ответ с информацией о выполненной операции начисления комиссии.
        """
        request = MakeFeeOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),  # Генерация случайной суммы
            status=fake.proto_enum(OperationStatus)  # Статус операции
        )
        return self.make_fee_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """
        Выполнение операции покупки.

        :param card_id: Идентификатор карты, с которой выполняется покупка.
        :param account_id: Идентификатор счёта, с которого выполняется покупка.
        :return: Ответ с информацией о выполненной операции покупки.
        """
        request = MakePurchaseOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),  # Генерация случайной суммы
            status=fake.proto_enum(OperationStatus),  # Статус операции
            category=fake.category()  # Категория покупки
        )
        return self.make_purchase_operation_api(request)



def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())

def build_operations_gateway_locust_grpc_client(env: Environment) -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient с использованием Locust.

    :param env: Окружение Locust.
    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(env))