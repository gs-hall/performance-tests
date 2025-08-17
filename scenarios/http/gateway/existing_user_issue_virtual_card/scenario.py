from locust import task, events
from locust.env import Environment
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from seeds.scenarios.existing_user_issue_virtual_card import ExistingUserIssueVirtualCardSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser
from clients.http.gateway.accounts.schema import (
    AccountSchema,
    AccountType
)

# Хук инициализации — вызывается перед началом запуска нагрузки
@events.init.add_listener
def init(environment: Environment, **kwargs):
    # Выполняем сидинг
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()

    # Загружаем результат сидинга (из файла JSON)
    environment.seeds = seeds_scenario.load()

# 1. Получение списка счетов;
# 2. Выпуск новой виртуальной карты.


# TaskSet — сценарий пользователя. Каждый виртуальный пользователь выполняет эти задачи
class IssueVirtualCardTaskSet(GatewayHTTPSequentialTaskSet):
    """
    Сценарий для выпуска виртуальной карты для существующего пользователя.
    Последовательно выполняет следующие шаги:
    1. Получает список счетов пользователя.
    2. Выпускает виртуальную карту для дебетового счёта.
    """

    seed_user: SeedUserResult  # Типизированная ссылка на данные из сидинга

    # Shared state — сохраняем результаты запросов для дальнейшего использования
    accounts: list[AccountSchema] = None

    def on_start(self) -> None:
        super().on_start()
        # Получаем случайного пользователя из подготовленного списка
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(3)
    def get_accounts(self):
        """
        Получаем список счетов пользователя.
        Сохраняем результат в shared state для дальнейшего использования.
        """
        response = self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)
        self.accounts = response.accounts  # Сохраняем счета в shared state

    @task(1)
    def issue_virtual_card(self):
        """
        Выпускаем виртуальную карту для дебетового счёта.
        Проверяем, что у пользователя есть хотя бы один дебетовый счёт.
        """
        if not self.accounts:
            return  # Если счета не получены, нет смысла продолжать

        debit_accounts = [account for account in self.accounts if account.type == AccountType.DEBIT_CARD]
        if not debit_accounts:
            print("No debit accounts found for user:", self.seed_user.user_id)
            return  # Если нет дебетовых счетов, ничего не делаем

        # Выпускаем виртуальную карту для первого дебетового счёта
        self.cards_gateway_client.issue_virtual_card(
            user_id=self.seed_user.user_id,
            account_id=debit_accounts[0].id
        )

class IssueVirtualCardScenarioUser(LocustBaseUser):
    """
    Пользователь, выполняющий сценарий выпуска виртуальной карты.
    Использует IssueVirtualCardTaskSet для выполнения задач.
    """
    tasks = [IssueVirtualCardTaskSet]
