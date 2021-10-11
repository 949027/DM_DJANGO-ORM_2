# Пульт охраны банка
Отбражение активных карт доступа, списка активных карт доступа, списка посещений по карте доступа

### Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл .env рядом с manage.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.
Необходимые переменные окружения: ```HOST, PASSWORD, SECRET_KEY, DEBUG```.

### Как запустить
Запустите сервер командой 
```python
 manage.py runserver 0.0.0.0:8000
 ```
 после чего наберите в адресной строке браузера ```http://127.0.0.1:8000/```.

### Как использовать
С помощью браузера вы можете просмотреть:
- список активных карт доступа
- список пользователей в хранилище
- список посещений по каждой карте доступа