from locust import task

from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from clients.http.gateway.operations.schema import MakeTopUpOperationResponseSchema
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser

# Класс сценария: описывает последовательный флоу нового пользователя
# Сценарий включаtn последовательное выполнение следующих шагов:
# Создание нового пользователя;
# Открытие дебетового счёта для этого пользователя;
# Выпуск физической карты, привязанной к этому счёту.

class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    """
    Класс сценария: описывает последовательный флоу нового пользователя
    Сценарий включает последовательное выполнение следующих шагов:
    1. Создание нового пользователя;
    2. Открытие дебетового счёта для этого пользователя;
    3. Выпуск физической карты, привязанной к этому счёту.
    """
    # Храним ответы от предыдущих шагов, чтобы использовать их в следующих задачах
    create_user_response: CreateUserResponseSchema | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponseSchema | None = None

    @task
    def create_user(self):
        # Первый шаг — создать нового пользователя
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        # Невозможно открыть счёт без созданного пользователя
        if not self.create_user_response:
            return
        # Открываем дебетовый счёт для нового пользователя
        self.open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def issue_physical_card(self):
        # Проверяем, что счёт успешно открыт
        if not self.open_debit_card_account_response:
            return

        # Выпускаем физическую карту, привязанную к дебетовому счёту
        self.cards_gateway_client.issue_physical_card(
            user_id=self.create_user_response.user.id,
            account_id=self.open_debit_card_account_response.account.id
        )

class IssuePhysicalCardScenarioUser(LocustBaseUser):
    """
    Класс пользователя сценария: наследуется от LocustBaseUser и использует
    IssuePhysicalCardSequentialTaskSet для выполнения сценария.
    """
    tasks = [IssuePhysicalCardSequentialTaskSet]
