import requests

url = 'http://127.0.0.1:8000/api/token/'
data = {
    'username': 'admin',
    'password': 'admin'
}

response = requests.post(url, data=data)

if response.status_code == 200:
    tokens = response.json()
    access_token = tokens['access']
    print('Access token:', access_token)
else:
    print('Failed to get token:', response.status_code)
