from seeds.scenario import SeedsScenario
from seeds.schema.plan import (
  SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan, SeedOperationsPlan,
)

class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который просматривает свои операции.
    1. Уже существующий пользователь входит в приложение.
    2. Он загружает список своих счетов.
    3. У пользователя должен быть один кредитный счёт.

    Для каждого кредитного счёта должно быть:
    - 5 операций покупки.
    - 1 операция пополнения счёта.
    - 1 операция снятия наличных.

    Создаёт 300 пользователей, каждому из которых открывается кредитный счёт и кредитная карта.
    """
    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга, который описывает, сколько пользователей нужно создать
        и какие именно данные для них генерировать.
        В данном случае создаём 300 пользователей, каждому выдаём кредитный счёт и кредитную карту.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Количество пользователей
                credit_card_accounts=SeedAccountsPlan(
                    count=1,  # Количество кредитных счетов на пользователя
                    physical_cards=SeedCardsPlan(count=1),  # Количество физических карт на пользователя
                    purchase_operations=SeedOperationsPlan(count=5),  # 5 операций покупки на счёт
                    top_up_operations=SeedOperationsPlan(count=1),  # 1 операция пополнения счёта
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),  # 1 операция снятия наличных
                ),
            ),
        ),


    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_get_operations"

if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга