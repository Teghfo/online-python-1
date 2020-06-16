import requests


response = requests.post('http://localhost:5001/10multiply', data={'number': 87})

print(response.content)