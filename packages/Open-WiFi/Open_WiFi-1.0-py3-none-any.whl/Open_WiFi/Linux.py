import subprocess as sp
import platform

def wifi_names():
    # Запись вывода в переменную, с терминала, по запросу вывода всех файлов хранящих пароль от точек доступа
    list_all_wifi_names = sp.check_output('cd /etc/NetworkManager/system-connections/ && ls', shell=True)

    # Очистка лишнего и получения названия файлов, подключённых сетей
    list_all_wifi_names = str(list_all_wifi_names).split("b'")[1]
    list_all_wifi_names = str(list_all_wifi_names).split("'")[0]
    list_all_wifi_names = str(list_all_wifi_names).split('\\n')[0:-1]

    return list_all_wifi_names



def passwords(wifi_name):
    # Запись вывода в переменную, с терминала, по запросу вывода информации о конкретной точки доступа
    info_of_wifi = sp.check_output(f'cd /etc/NetworkManager/system-connections/ && sudo cat {wifi_name}', shell=True)

    # Проверка на наличие пароля, или его отсутствия
    try:
        password = str(info_of_wifi).split('psk=')[1]
        password = str(password).split('\\n\\n[ipv4]')[0]
    except:
        password = 'Отсутствует'

    return password



def main():
    # Список хронящий все имена и пароли wifi сетей
    list_wifi = []

    if platform.system() == 'Linux':
        # Цикл получения спика всех имён сетей, и их пароля
        for wifi_name in wifi_names():
            name = wifi_name.split('.nmconnection')[0]
            password = passwords(wifi_name)
            list_wifi.append([name, password])

    else: list_wifi.append('Упс, похоже что Вы запускаете не с Linux!')

    return list_wifi



if __name__ == '__main__':
    main()