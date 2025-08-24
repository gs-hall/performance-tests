from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client

# Создать пользователя с помощью метода клиента UsersGatewayHTTPClient.create_user
users_gateway_client = build_users_gateway_http_client()
create_user_response = users_gateway_client.create_user()
user_id = create_user_response.user.id  # Извлекаем user_id из ответа
print('Create user response:', create_user_response)
print('User ID:', user_id)


# Открыть кредитный счет AccountsGatewatHTTPClient.open_credit_card_account
accounts_gateway_client = build_accounts_gateway_http_client()
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(user_id)
account_id = open_credit_card_account_response.account.id
print('Open credit card account response:', open_credit_card_account_response)
print('Account ID:', account_id)

# Получает документ тарифа
documents_gateway_client = build_documents_gateway_http_client()
get_tariff_document_response = documents_gateway_client.get_tariff_document(account_id)
print('Get tariff document response:', get_tariff_document_response)
get_documents_response = documents_gateway_client.get_tariff_document(account_id)
print('Get document data:', get_documents_response)
print('Tariff document:', get_documents_response.tariff.document)

# Получает документ контракта
get_contract_document_response = documents_gateway_client.get_contract_document(account_id)
print('Get contract document response:', get_contract_document_response)
print('Contract Document:', get_contract_document_response.contract.document)
