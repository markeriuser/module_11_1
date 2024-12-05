import requests

# 1. Отправка GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.json())  # Выводим данные в формате JSON

# 2. Отправка POST-запроса
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.json())  # Выводим ответ сервера

# 3. Обработка параметров запроса
params = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(response.json())  # Выводим посты пользователя с ID = 1
