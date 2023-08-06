`roblox-dev` - Модуль позволяющий управлять, писать сообщение через код в 'python'

для начала сделаем файл для авторизации:

```py
from roblox_dev import roblox_login

# Создание экземпляра класса roblox_login
username = "my_username"
password = "my_password"
roblox = roblox_login(username, password)

# Авторизация
roblox.login()


Для управления, или отправление сообщение нам нужен файл для контроля:

```py
from roblox_dev import server

# Создание экземпляра класса `server`
server_url = "https://www.roblox.com/games/1234567890/my-game"
roblox_server = server(server_url)

# Подключение к серверу
roblox_server.join()

# Отключение от сервера
roblox_server.leave()

# Управление сервером
command = "move forward"
roblox_server.controller(command)

# Отправка сообщения в чат на сервере
message = "Hello, everyone!"
roblox_server.message_send(message)

