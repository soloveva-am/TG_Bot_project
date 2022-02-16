import requests

url = 'http://wttr.in/?T'

response = requests.get (url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа
