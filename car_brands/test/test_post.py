import requests

data = {
    "name": "3",
    "country": "Germany",
    "info": "Made in Germany"
}

response = requests.post('http://127.0.0.1:8000/cars/add/', json=data)

if response.status_code == 201:
    print('Car brand created successfully')
    car_brand = response.json()
    print(car_brand)
else:
    print(f'Failed to create car brand. Status code: {response.status_code}')
    print(response.text)
