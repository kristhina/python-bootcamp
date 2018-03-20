import requests

result = requests.post(
    'http://localhost:5000/user/python/set-password',
    json=('password':'witam')
)
print(result.text)