import requests

url = 'http://127.0.0.1:8000/cars/2/'
headers = {
    'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NDU3NDgyLCJpYXQiOjE3MjU0NTYyODIsImp0aSI6IjNlYTYwMzc3Y2U2YzQ2ZWJiZTUxYzk1Y2ZmMTcwNjFmIiwidXNlcl9pZCI6MX0.X9tKWk8uym4ZEWanxvLY9OTMwr3GDLREAf1cWcwLmcM',
}

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print('Car brand deleted successfully')
else:
    print(f'Failed to delete car brand. Status code: {response.status_code}, Response: {response.text}')
