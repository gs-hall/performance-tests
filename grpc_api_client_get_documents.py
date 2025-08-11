from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.documents.client import build_documents_gateway_grpc_client

# 1. Создать пользователя с помощью метода клиента UsersGatewayGRPCClient.create_user.

# Создаём gRPC API-клиент для взаимодействия с UsersGatewayService
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
documents_gateway_client = build_documents_gateway_grpc_client()

# Создаём пользователя с помощью клиентского метода create_user
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# 2. Открыть кредитный счёт с помощью метода AccountsGatewayGRPCClient.open_credit_card_account.
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
    user_id=create_user_response.user.id
)
print('Open credit card account response:', open_credit_card_account_response)

# 3. Получить документ тарифа через метод DocumentsGatewayGRPCClient.get_tariff_document.
tariff_document_response = documents_gateway_client.get_tariff_document(
    account_id=open_credit_card_account_response.account.id
)
print('Get tariff document response:', tariff_document_response)

# 4. Получить документ контракта через метод DocumentsGatewayGRPCClient.get_contract_document.
contract_document_response = documents_gateway_client.get_contract_document(
    account_id=open_credit_card_account_response.account.id
)
print('Get contract document response:', contract_document_response)