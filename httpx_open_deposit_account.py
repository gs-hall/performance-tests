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
    "http://localhost:8003/api/v1/accounts/open-debit-card-account",
    json=create_account_request
)
create_account_response_data = create_account_response.json()
create_account_response_code = create_account_response.status_code

print("Create user response:", create_user_response_data)
print("Create user code:", create_user_response_code)

print("Create account response:", create_account_response_data)
print("Create account code:", create_account_response_code)
