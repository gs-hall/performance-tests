
# Performance Tests

Этот проект помогает проводить нагрузочное тестирование с помощью [Locust](https://locust.io/).
Код нагрузочных тестов написан на Python.
Ссыылка на стенд: [Performance QA Engineer Course](https://github.com/Nikita-Filonov/performance-qa-engineer-course)

## Организация проекта

Код организован по слоям архитектуры:

- **Клиенты**: Реализуют взаимодействие с API по протоколам HTTP или GRPC (каталог **clients**)
- **Сидинг**: Подготавливают тестовые данные через GRPS-клиентов (каталог **seeds**)
- **Сценарии**: Определяют поведение пользователей, сценарии группируются в группы задач для HTTP- и GRPC-клиентов (каталог **scenarios**)
- **Инструменты**: Включает хэлперы для создания тестовых данных, конфигурирования и общую логику работы с Locust'ом (каталог **tools**)

## Сценарии

Сценарии делятся на:

- сценарии для существующих пользователей (имеют префикс existing_user), такие сценарии требуют сидинга тестовых данных
- сценарии для новых пользователей (имеют префикс new_user), такие сценарии создают тестовые данные сами

## Подготовка к запуску

### Как склонировать и открыть проект

git clone <https://github.com/gs-hall/performance-tests>
cd performance-tests
code .

### Настройка окружения

Для активации виртуального окружения Python нужно выполнить команду:
source venv/bin/activate

### Установка зависимостей

pip install -r requirements.txt

## Запуск тестов

### Примеры команд для запуска нагрузочных тестов

Примеры запуска нагрузочного теста для GRPC/HTTP без сидинга (т.е. без подготовки данных - для новых пользователей):
locust --config=./scenarios/grpc/gateway/new_user_get_documents/v1.0.conf
locust --config=./scenarios/http/gateway/new_user_get_documents/v1.0.conf

Примеры запуска нагрузочного теста для GRPC/HTTP с предварителоьным сидингом (т.е. с подготовкой тестовых данных для существующих пользователей):
locust --config=./scenarios/grpc/gateway/existing_user_get_documents/v1.0.conf
locust --config=./scenarios/http/gateway/existing_user_get_documents/v1.0.conf

### Просмотр отчетов

Отчеты автоматически сохраняются в папку сценария теста.
Например, можно открыть отчет:
scenarios/grpc/gateway/existing_user_get_documents/report.html

### Мониторинг работы стенда во время тестов

Данный проект не содерджит средств мониторинга, но можно воспользоваться средствами наблюдаемости, заложенными в тестируемый стенд [Performance QA Engineer Course](https://github.com/Nikita-Filonov/performance-qa-engineer-course):

- **Grafana:** <http://localhost:3002>
- **Prometheus:** <http://localhost:9090>
