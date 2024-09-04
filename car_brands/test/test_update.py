import requests

url = 'http://127.0.0.1:8000/cars/1/'
data = {
    "name": "BMW Updated",
    "country": "Germany",
    "info": "Updated Info"
}
headers = {
    'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDU3NDgyLCJpYXQiOjE3MjU0NTYyODIsImp0aSI6IjNlYTYwMzc3Y2U2YzQ2ZWJiZTUxYzk1Y2ZmMTcwNjFmIiwidXNlcl9pZCI6MX0.X9tKWk8uym4ZEWanxvLY9OTMwr3GDLREAf1cWcwLmcM',
    'Content-Type': 'application/json'
}

response = requests.put(url, json=data, headers=headers)

if response.status_code == 200:
    print('Car brand updated successfully:', response.json())
else:
    print(f'Failed to update car brand. Status code: {response.status_code}, Response: {response.text}')