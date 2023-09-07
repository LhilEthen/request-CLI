import requests
from getpass import getpass
from time import sleep


endpoint: str = 'http://127.0.0.1:9000/hmm/'
post_ednpoint: str = 'http://127.0.0.1:9000/add/' 
create_endpoint: str = 'http://127.0.0.1:9000/create/'
auth_endpiont: str = 'http://127.0.0.1:9000/auth/'

get_all_products: str = 'http://127.0.0.1:9000/products/'

# get_response = requests.post(endpoint, json={'username':'lemon', 'password':'123'})
# data: str = input("what do you wanna add to the database ")

get_all_products_data = requests.get(get_all_products)
print(get_all_products_data.json())
print(get_all_products_data)

username = input('Enter username ')
get_password = getpass('Please enter password ')

get_auth = requests.post(auth_endpiont, json={'username':username, 'password':get_password})
print(get_auth.json())
# get_data_added = requests.get(post_ednpoint)

# print(add_data.json())
# # print(add_data.)
# get_response = requests.get(endpoint, params={"param":"kofi"})

# print(get_response.json())
# print(get_response.headers)

# print(get_response.json())    
# if get_response.status_code == "200":
#     print("OK")
# else:
#     print("NOT OHK")
#     print(get_response.status_code)

# print(get_response.headers)

# print(type(get_response))

# print(dict(endpoint))