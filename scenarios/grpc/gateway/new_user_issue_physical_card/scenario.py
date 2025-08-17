from locust import task

from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from tools.locust.user import LocustBaseUser

class IssuePhysicalCardSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    """
    Выполняет сценарий, в котором пользователь получает физическую карту.
    Сценарий включает в себя создание пользователя, открытие счета и выпуск физической карты.
    1. Создание нового пользователя;
    2. Открытие дебетового счёта для этого пользователя;
    3. Выпуск физической карты, привязанной к этому счёту.
    """
     # Храним ответы от предыдущих шагов, чтобы использовать их в следующих задачах
    create_user_response: CreateUserResponse | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponse | None = None

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
