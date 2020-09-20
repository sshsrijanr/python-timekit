from timekit import TimekitAPI

client = TimekitAPI(app_token="test_api_key_pJ7DDjTeWT9e7TbvqZFF2MtYHnRqDlmP")
response = client.bookings.list()
assert response.status in range(200, 206)
client.bookings.groups.list()