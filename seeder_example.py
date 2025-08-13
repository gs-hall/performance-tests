# Импорт фабрики для создания сидера на gRPC-клиентах
from seeds.builder import build_grpc_seeds_builder

# Импорт схемы плана сида — описывает, какие сущности и в каком количестве нужно создать
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan

# Шаг 1: создаём билдер с использованием gRPC-протокола
builder = build_grpc_seeds_builder()

# Шаг 2: вызываем метод .build(), передаём в него план генерации данных
result = builder.build(
    SeedsPlan(
        users=SeedUsersPlan(
            count=500,  # Нужно создать 500 пользователей
            credit_card_accounts=SeedAccountsPlan(
                count=1,  # У каждого пользователя — один кредитный счёт
                physical_cards=SeedCardsPlan(count=1),  # На счёте одна физическая карта
            )
        ),
    )
)

# Шаг 3: выводим результат — структура, содержащая идентификаторы созданных пользователей, счетов, карт и операций
print(result)
