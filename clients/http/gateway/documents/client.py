from httpx import Response

from typing import TypedDict

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client  # Импортируем builder

# Пример структуры ответа для получения документа тарифа
# {
#   "tariff": {
#     "url": "https://example.com/",
#     "document": "string"
#   }
# }

class DocumentDict(TypedDict):
    """
    Описание структуры документа.
    """
    url: str
    document: str

class GetTariffDocumentResponseDict(TypedDict):
    """
    Описание структуры документа тарифа.
    """
    tariff: DocumentDict

class GetContractDocumentResponseDict(TypedDict):
    """
    Описание структуры документа контракта.
    """
    tariff: DocumentDict

class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить документ тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Словарь с данными документа тарифа.
        """
        response = self.get_tariff_document_api(account_id)
        response.raise_for_status()
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить документ контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Словарь с данными документа контракта.
        """
        response = self.get_contract_document_api(account_id)
        response.raise_for_status()
        return response.json()


# Добавляем builder для DocumentsGatewayHTTPClient
def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())