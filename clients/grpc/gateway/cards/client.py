from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest, IssuePhysicalCardResponse
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2_grpc import CardsGatewayServiceStub
from tools.fakers import fake

class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с CardsGatewayService.
    Предоставляет высокоуровневые методы для выпуска физических карт.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к CardsGatewayService.
        """
        super().__init__(channel)
        self.stub = CardsGatewayServiceStub(channel)  # gRPC-стаб, сгенерированный из .proto

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """
        Низкоуровневый вызов метода IssuePhysicalCard через gRPC.

        :param request: gRPC-запрос с данными для выпуска карты.
        :return: Ответ от сервиса с информацией о выпущенной карте.
        """
        return self.stub.IssuePhysicalCard(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        """
        Выпуск физической карты для указанного пользователя и счёта.

        :param user_id: Идентификатор пользователя, для которого выпускается карта.
        :param account_id: Идентификатор счёта, к которому привязывается карта.
        :return: Ответ с информацией о выпущенной карте.
        """
        request = IssuePhysicalCardRequest(
            user_id=user_id,
            account_id=account_id,
            cardholder_name=fake.name(),
            card_type=fake.card_type()
        )
        return self.issue_physical_card_api(request)

    def issue_virtual_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """
        Низкоуровневый вызов метода IssueVirtualCard через gRPC.

        :param request: gRPC-запрос с данными для выпуска виртуальной карты.
        :return: Ответ от сервиса с информацией о выпущенной виртуальной карте.
        """
        return self.stub.IssueVirtualCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        """
        Выпуск виртуальной карты для указанного пользователя и счёта.

        :param user_id: Идентификатор пользователя, для которого выпускается карта.
        :param account_id: Идентификатор счёта, к которому привязывается карта.
        :return: Ответ с информацией о выпущенной виртуальной карте.
        """
        request = IssuePhysicalCardRequest(
            user_id=user_id,
            account_id=account_id,
            cardholder_name=fake.name(),
            card_type=fake.card_type()
        )
        return self.issue_virtual_card_api(request)

def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра CardsGatewayGRPCClient.

    :return: Инициализированный клиент для CardsGatewayService.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_grpc_client())
