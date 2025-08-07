from clients.http.gateway.cards import CardsGatewayHTTPClient, IssueVirtualCardRequestDict, IssuePhysicalCardRequestDict


cards_api = CardsGatewayHTTPClient()
issue_virtual_card_request: IssueVirtualCardRequestDict = {
    "userId": "example_user_id",
    "accountId": "example_account_id"
}
response = cards_api.issue_virtual_card_api(issue_virtual_card_request)
print("Issue Virtual Card Response:", response.json())
print("Issue Virtual Card Status Code:", response.status_code)
issue_physical_card_request: IssuePhysicalCardRequestDict = {
    "userId": "example_user_id",
    "accountId": "example_account_id"
}
response = cards_api.issue_physical_card_api(issue_physical_card_request)
print("Issue Physical Card Response:", response.json())
print("Issue Physical Card Status Code:", response.status_code)