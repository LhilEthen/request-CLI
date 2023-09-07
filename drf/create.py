import requests


endpiont: str = 'http://127.0.0.1:9000/create-product/'

post_data: None = requests.post(endpiont, json={'name':'AppleBooks', 'price':6758})
print(post_data)