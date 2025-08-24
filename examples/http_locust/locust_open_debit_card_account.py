from locust import User, between, task
from tools.fakers import fake  # генератор случайных данных
from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema

class OpenDebitCardAccountScenarioUser(User):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)

    host = "localhost"  # фиктивный host для запросов

    # В этой переменной будем хранить экземпляр нашего API клиента для работы с пользователями
    user_gateway_client: UsersGatewayHTTPClient

    # В этой переменной будем хранить экземпляр нашего API клиента для работы со счетами
    accounts_gateway_client: AccountsGatewayHTTPClient

    # Поле, куда мы сохраним ответ после создания пользователя
    create_user_response: CreateUserResponseSchema

    # Поле, куда мы сохраним данные счета после открытия дебетовой карты
    account_data: OpenDebitCardAccountResponseSchema

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        # создаем API клиент, встроенный в экосистему Locust (с хуками и поддержкой сбора метрик)
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)

        # создаем пользователя через API
        self.create_user_response = self.users_gateway_client.create_user()

        # создаем API клиент для работы со счетами
        # используем тот же environment, чтобы Locust мог собирать метрики
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)

    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача: открытие дебетовой карты.
        Здесь мы выполняем POST-запрос к /api/v1/accounts/open-debit-card-account.
        """
        self.account_data = self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user_id)