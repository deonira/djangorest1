import requests


access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1Mjg1MDA2LCJpYXQiOjE3MjUyODQ5OTEsImp0aSI6IjA1NmJmODBiZmVmODRhZjNhYzA0YzAwYWI1N2I1NDhjIiwidXNlcl9pZCI6MX0.K6NDL7bbhJwSv7LJ2FGBurCE0lt9neQRe1ZNzKnB9to'

url_car = 'http://127.0.0.1:8000/add/'
data_car = {
    "name": "BMW1",
    "country": "Germany",
    "info": "Made in Germany"
}
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response_car = requests.post(url_car, json=data_car, headers=headers)

if response_car.status_code == 201:
    print('Car brand created successfully:', response_car.json())
else:
    print(f'Failed to create car brand. Status code: {response_car.status_code}, Response: {response_car.text}')