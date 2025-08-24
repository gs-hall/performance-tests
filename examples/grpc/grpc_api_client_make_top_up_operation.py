from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client

# Создаём gRPC API-клиент для взаимодействия с UsersGatewayService
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
operations_gateway_client = build_operations_gateway_grpc_client()

# 1. Создать пользователя с помощью метода клиента UsersGatewayGRPCClient.create_user.
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# 2. Открыть дебетовый счет  AccountsGatewatGRPCClient.open_credit_card_account.
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response.user.id
)
print('Open debit card account response:', open_debit_card_account_response)

# 3. Создать операцию пополнения счета OperationsGatewayGRPCClient.make_top_up_operations.
make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    card_id=open_debit_card_account_response.account.cards[0].id,
    account_id=open_debit_card_account_response.account.id,
)
print('Make top up operation response:', make_top_up_operation_response)