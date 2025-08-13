from locust import User, between, task

# Импортируем схемы ответов, чтобы типизировать shared state
from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from tools.locust.user import LocustBaseUser  # Импортируем базовый класс

class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    Нагрузочный сценарий, который в произвольном порядке:
    1. Создаёт нового пользователя.
    2. Открывает депозитный счёт.
    3. Запрашивает список всех счетов.

    Использует базовый GatewayGRPCTaskSet и уже созданных в нём API клиентов.
    """

    # Shared state — сохраняем результаты запросов для дальнейшего использования
    create_user_response: CreateUserResponse | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что предыдущий шаг был успешным.
        """
        if not self.create_user_response:
            return  # Если пользователь не был создан, нет смысла продолжать

        self.accounts_gateway_client.open_deposit_account(
            user_id=self.create_user_response.user.id
        )

    @task(6)
    def get_documents(self):
        """
        Запрашиваем список всех счетов.
        """
        if not self.create_user_response:
            return  # Если пользователь не был создан, нет смысла продолжать

        self.accounts_gateway_client.get_accounts(
            user_id=self.create_user_response.user.id
        )


class GetDocumentsScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения документов.
    """
    tasks = [GetAccountsTaskSet]
