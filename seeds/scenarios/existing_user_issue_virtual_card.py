from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan

class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который получает виртуальную карту.
    Уже существующий пользователь входит в приложение.
    Он загружает список своих счетов.
    У пользователя должен быть один дебетовый счёт.
    Затем пользователь выполняет выпуск виртуальной карты для своего дебетового счёта.
    Создаёт 300 пользователей, каждому из которых выдается виртуальная карта.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга, который описывает, сколько пользователей нужно создать
        и какие именно данные для них генерировать.
        В данном случае создаём 300 пользователей, каждому выдаём дебетовый счёт и виртуальную карту.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Количество пользователей
                debit_card_accounts=SeedAccountsPlan(
                    count=1,  # Количество дебетовых счетов на пользователя
                    virtual_cards=SeedCardsPlan(count=1)  # Количество виртуальных карт на пользователя
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_issue_virtual_card"

if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга