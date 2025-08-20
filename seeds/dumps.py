import os

from seeds.schema.result import SeedsResult
from tools.logger import get_logger

logger = get_logger("SEEDS_DUMPS")

def save_seeds_result(result: SeedsResult, scenario: str):
    """
    Сохраняет результат сидинга (SeedsResult) в JSON-файл.

    :param result: Результат сидинга, сгенерированный билдером.
    :param scenario: Название сценария нагрузки, для которого создаются данные.
                     Используется для генерации имени файла (например, "credit_card_test").
    """
    # Убедимся, что папка dumps существует
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    # Сохраняем результат сидинга в файл с именем {scenario}_seeds.json
    file_path = f"./dumps/{scenario}_seeds.json"
    with open(file_path, 'w+', encoding="utf-8") as file:
        file.write(result.model_dump_json())
    logger.debug(f"Seeding result saved to file: {file_path}")


def load_seeds_result(scenario: str) -> SeedsResult:
    """
    Загружает результат сидинга из JSON-файла.

    :param scenario: Название сценария нагрузки, данные которого нужно загрузить.
    :return: Объект SeedsResult, восстановленный из файла.
    """
    # Открываем файл и валидируем его как объект SeedsResult
    file_path = f"./dumps/{scenario}_seeds.json"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Seeds result file not found: {file_path}")

    logger.debug(f"Loading seeding result from file: {file_path}")
    with open(f'./dumps/{scenario}_seeds.json', 'r', encoding="utf-8") as file:
        return SeedsResult.model_validate_json(file.read())
    logger.debug(f"Seeding result loaded from file: {file_path}")