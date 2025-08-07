from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client


# Создать пользователя с помощью метода клиента UsersGatewayHTTPClient.create_user
users_gateway_client = build_users_gateway_http_client()
create_user_response = users_gateway_client.create_user()
user_id = create_user_response['user']['id']
print('Create user response:', create_user_response)
print('User ID:', user_id)

# Открыть дебетовый счет с помощью метода клиента AccountsGatewatHTTPClient.open_credit_card_account
accounts_gateway_client = build_accounts_gateway_http_client()
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(user_id)
print('Open debit card account response:', open_credit_card_account_response)

accountId = open_credit_card_account_response['account']['id']
cardId = open_credit_card_account_response['account']['cards'][0]['id']
print('Account ID:', accountId)
print('Card ID:', cardId)

# Создать операцию пополнения счета OperationsGatewayHTTPClient.make_top_up_operations
operations_gateway_client = build_operations_gateway_http_client()
make_top_up_operation_request = {"accountId": accountId, "amount": 1000, "status": "COMPLETED", "cardId": cardId}
make_top_up_operation_response = operations_gateway_client.make_top_up_operation(make_top_up_operation_request)
print('Make top up operation response:', make_top_up_operation_response)