import requests

kot = requests.get("http://py.net/cat")
with open('kot.jpg', 'wb') as file:
    file.write(kot.content)