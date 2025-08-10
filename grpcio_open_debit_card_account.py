import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub

from tools.fakers import fake  # Используем генератор фейковых данных, созданный ранее

# Устанавливаем соединение с gRPC-сервером по адресу localhost:9003
channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиент для UsersGatewayService
users_gateway_service = UsersGatewayServiceStub(channel)

# Создать нового пользователя
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

# Открыть дебетовый аккаунт
accounts_gateway_service = AccountsGatewayServiceStub(channel)
# Формируем запрос на открытие дебетового аккаунта с использованием ID пользователя
open_debit_card_account_request = OpenDebitCardAccountRequest(
    user_id=create_user_response.user.id,
)
# Отправляем запрос и получаем ответ
open_debit_card_account_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(open_debit_card_account_request)
print('Open debit card account response:', open_debit_card_account_response)