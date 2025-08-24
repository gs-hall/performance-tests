import time
import httpx

# Create user
create_user_request = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "last",
    "firstName": "first",
    "middleName": "middle",
    "phoneNumber": "1234567890",
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_request)
create_user_response_data = create_user_response.json()
create_user_response_code = create_user_response.status_code

# Create account
create_account_request = {
    "userId": create_user_response_data["user"]["id"]
}
create_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=create_account_request
)
create_account_response_data = create_account_response.json()
create_account_response_code = create_account_response.status_code
accountId = create_account_response_data["account"]["id"]
cardId = create_account_response_data["account"]["cards"][0]["id"]

# Make a purchase
purchase_request = {
    "status": "IN_PROGRESS",
    "accountId": accountId,
    "cardId": cardId,
    "amount": 77.99,
    "category": "taxi"
}
purchase_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=purchase_request
)
purchase_response_data = purchase_response.json()
purchase_response_code = purchase_response.status_code
operationId = purchase_response_data["operation"]["id"]

# Get receipt
get_receipt_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{operationId}"
)
get_receipt_response_data = get_receipt_response.json()
get_receipt_response_code = get_receipt_response.status_code

# Output the results
print("Create user response:", create_user_response_data)
print("Create user code:", create_user_response_code)

print("Create account response:", create_account_response_data)
print("Create account code:", create_account_response_code)
print("Account ID:", accountId)
print("Card ID:", cardId)

print("Purchase response:", purchase_response_data)
print("Purchase code:", purchase_response_code)
print("Operation ID:", operationId)

print("Get receipt response:", get_receipt_response_data)
print("Get receipt code:", get_receipt_response_code)
print("Receipt content:", get_receipt_response_data.get("receipt", "No receipt found"))