import requests


url_car = 'http://127.0.0.1:8000/add/'
data_car = {
    "name": "BMW1",
    "country": "Germany",
    "info": "Made in Germany"
}
headers = {
    'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDU3NDgyLCJpYXQiOjE3MjU0NTYyODIsImp0aSI6IjNlYTYwMzc3Y2U2YzQ2ZWJiZTUxYzk1Y2ZmMTcwNjFmIiwidXNlcl9pZCI6MX0.X9tKWk8uym4ZEWanxvLY9OTMwr3GDLREAf1cWcwLmcM',
    'Content-Type': 'application/json'
}

response_car = requests.post(url_car, json=data_car, headers=headers)

if response_car.status_code == 201:
    print('Car brand created successfully:', response_car.json())
else:
    print(f'Failed to create car brand. Status code: {response_car.status_code}, Response: {response_car.text}')