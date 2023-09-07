import requests
from getpass import getpass

list_endpoint: str = 'http://127.0.0.1:9000/products/'
auth_endpiont: str = 'http://127.0.0.1:9000/auth/'


username: str = input('input username ')
password: str = getpass('enter password ')
get_auth_token = requests.post(auth_endpiont, json={'username':username, 'password':password})
access_token = get_auth_token.json().get('access')
print(get_auth_token.json())
print(access_token)

get_data = requests.get(list_endpoint, headers={'Authorization': f'Bearer {access_token}'})

print(get_data.json())