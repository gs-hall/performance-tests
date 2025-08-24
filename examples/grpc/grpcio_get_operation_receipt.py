import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (GetOperationReceiptRequest, GetOperationReceiptResponse)


from contracts.services.operations.operation_pb2 import OperationStatus
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub

from tools.fakers import fake  # Используем генератор фейковых данных, созданный ранее

# Устанавливаем соединение с gRPC-сервером по адресу localhost:9003
channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиент для Users, Accounts и Operations сервисов
users_gateway_service = UsersGatewayServiceStub(channel)
operations_gateway_service = OperationsGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
documents_gateway_service = DocumentsGatewayServiceStub(channel)

# 1. Создать нового пользователя
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)

# Отправляем запрос и получаем ответ
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# Получить пользователя по ID, полученному из предыдущего ответа
get_user_request = GetUserRequest(id=create_user_response.user.id)
get_user_response: GetUserResponse = users_gateway_service.GetUser(get_user_request)
print('Get user response:', get_user_response)

# 2. Открыть дебетовый аккаунт

# Формируем запрос на открытие дебетового аккаунта с использованием ID пользователя
open_debit_card_account_request = OpenDebitCardAccountRequest(
    user_id=create_user_response.user.id,
)
# Отправляем запрос и получаем ответ
open_debit_card_account_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(open_debit_card_account_request)
print('Open debit card account response:', open_debit_card_account_response)

# 3. Пополнение счёта
make_top_up_operation_request = MakeTopUpOperationRequest(
    status=OperationStatus.OPERATION_STATUS_IN_PROGRESS,  # Статус операции (в процессе)
    amount=fake.amount(),  # Сумма покупки
    card_id=open_debit_card_account_response.account.cards[0].id,  # ID первой карты счёта
    account_id=open_debit_card_account_response.account.id,  # ID счёта
)
make_top_up_operation_response: MakeTopUpOperationResponse = operations_gateway_service.MakePurchaseOperation(
    make_top_up_operation_request
)
print('Make top up operation response:', make_top_up_operation_response)

# 4. Получение чека по операции
get_receipt_request = GetOperationReceiptRequest(
    operation_id=make_top_up_operation_response.operation.id  # ID операции, для которой получаем чек
)
get_receipt_response: GetOperationReceiptResponse = operations_gateway_service.GetOperationReceipt(get_receipt_request)
print('Get operation receipt response:', get_receipt_response)