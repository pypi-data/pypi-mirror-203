# <p align="center">Open_WiFi 🔐

<p align="center">Простой и в то же время полезный инструмент для получения списка всех имён сетей WiFi и их пароля, к которым когда-либо был подключён Ваш ПК!
<p align="center">Работает отлично как на Linux, так и на Windows! Но это ещё не всё, данный инструмент также работает и на Android!

## ⚡️ Установка

### Для Linux и Termux:
```python
pip3 install Open_WiFi
```

### Для Windows:
```python
pip install Open_WiFi
```
<br>

## 🌀 Использование

### Код на Python:
```python
import Open_WiFi

# Вызов функции получения всех имён wifi и их паролей
wifi = Open_WiFi.main()

# Вывод списка всей информации
print(wifi)
```
### Результат:
```python
>>> [['Network 1', 'Password'], ['TestNet', 'qwerty12'], ['Free WiFi', 'Отсутствует']]
```

### Другие примеры на Python:
```python
from Open_WiFi import WiFi

# Вызов функции получения всех имён wifi и их паролей исключительно на Windows
Windows = WiFi.main_windows()

# Вызов функции получения всех имён wifi и их паролей исключительно на Linux
Linux = WiFi.main_linux()

# Вызов функции получения всех имён wifi и их паролей исключительно на Android
Android = WiFi.main_android()
```
<br>

## 💎 Связь
 - **[Telegram](https://t.me/MY_INSIDE_DREAM)**
