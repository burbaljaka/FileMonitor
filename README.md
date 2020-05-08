# FileMonitor

Для запуска приложения нужно:
1. git clone https://github.com/burbaljaka/FileMonitor.git
2. cd FileMonitor
3. docker-compose up

Для указания отслеживаемой папки изменить PATH_TO_WATCH в файле settings.py проекта

Изменения каталога передаются по протоколу WS по адресу ws://127.0.0.1:8000/folder/
Для работы с websocket можно испрользовать расширение для Chrome - Simple WebSocket Client
