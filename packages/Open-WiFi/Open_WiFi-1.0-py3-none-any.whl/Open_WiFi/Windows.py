import subprocess as sp
import platform

def wifi_names():
    # Список, который будет хронить имена сетей Wi-Fi
    clean_list_all_wifi_names = []

    # Запись вывода в переменную, с терминала, по запросу вывода всех когда-либо подключённых точек доступа
    list_all_wifi_names = sp.check_output(['netsh', 'wlan', 'show', 'profiles'])

    # Цикл для получения чистого имени Wi-Fi сети
    for i in str(list_all_wifi_names).split('     '):
        if ': ' in i:
            red1 = i.split(': ')[1]
            if '\\r\\n' in red1: clean_list_all_wifi_names.append(red1.split('\\r\\n')[0])
            if "\\r\\n\\r\\n'" in red1: clean_list_all_wifi_names.append(red1.split("\\r\\n\\r\\n'")[0])

    return clean_list_all_wifi_names



def passwords(wifi_name):
    # Запись вывода в переменную, с терминала, по запросу вывода информации о конкретной точки доступа
    info_of_wifi = sp.check_output(['netsh', 'wlan', 'show', 'profiles', f'name={wifi_name}', 'key=clear'])

    # Очистка вывода от лишней информации, для получения чистого пароля
    password = str(info_of_wifi).split('          ')[-1]

    # Проверка на наличие пароля, или его отсутствия
    try:
        password = password.split('  : ')[1]
        password = password.split('\\r\\n\\r\\n')[0]
    except: password = 'Отсутствует'

    return password



def main():
    # Список хронящий все имена и пароли wifi сетей
    list_wifi = []

    if platform.system() == 'Windows':
        # Цикл получения спика всех имён сетей, и их пароля
        for wifi_name in wifi_names():
            password = passwords(wifi_name)
            list_wifi.append([wifi_name, password])

    else: list_wifi.append('Упс, похоже что Вы запускаете не с Windows!')
    
    return list_wifi



if __name__ == '__main__':
    main()