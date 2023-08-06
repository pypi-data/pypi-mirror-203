import subprocess as sp
import platform, os

def wifi_names():
    # Список, который будет хронить имена сетей Wi-Fi
    clean_list_all_wifi_names = []

    try:
        # Если версия Android'a менее 10
        try:
            # Запись вывода в переменную, с терминала, по запросу вывода информации хронящей нужные данные
            list_all_wifi = sp.check_output('sudo cat /data/misc/wifi/wpa_supplicant.conf', shell=True)

            # Очистка лишнего и получения названия файлов, подключённых сетей
            list_all_wifi = str(list_all_wifi).split('network=')[1:]
            for wifi_name in list_all_wifi:
                wifi_name = str(wifi_name).split('ssid="')[1]
                wifi_name = str(wifi_name).split('"')[0]
                clean_list_all_wifi_names.append(wifi_name)


        # Если версия Android'a более 10
        except:
            # Запись вывода в переменную, с терминала, по запросу вывода информации хронящей нужные данные
            list_all_wifi = sp.check_output('sudo cat /data/misc/apexdata/com.android.wifi/WifiConfigStore.xml', shell=True)

            # Очистка лишнего и получения названия файлов, подключённых сетей
            list_all_wifi = str(list_all_wifi).split('<string name="ConfigKey">&quot;')[1:]
            for wifi_name in list_all_wifi:
                wifi_name = str(wifi_name).split('&quot;WPA_PSK</string>')[0]
                if len(wifi_name) < 1000:
                    clean_list_all_wifi_names.append(wifi_name)
                else:
                    wifi_name = str(wifi_name).split('&quot;NONE</string>')[0]
                    clean_list_all_wifi_names.append(wifi_name)

    except: clean_list_all_wifi_names.append('Ошибка!')

    return clean_list_all_wifi_names



def passwords(wifi_name):
    # Если версия Android'a менее 10
    try:
        # Запись вывода в переменную, с терминала, по запросу вывода информации хронящей нужные данные
        list_all_wifi = sp.check_output('sudo cat /data/misc/wifi/wpa_supplicant.conf', shell=True)

        # Очистка лишнего и получения названия файлов, подключённых сетей
        wifi_pass = str(list_all_wifi).split(f'ssid="{wifi_name}"')[1]
        wifi_pass = str(wifi_pass).split(f'id_str="%7B%22creatorUid%22%3A%221000%22%2C%22configKey%22%3A%22%5C%22{wifi_name}%5C%22WPA_PSK%22%7D"')[0]
        try:
            wifi_pass = str(wifi_pass).split(f'psk="')[1]
            wifi_pass = str(wifi_pass).split(f'"')[0]
        except: wifi_pass = 'Отсутствует'


    # Если версия Android'a более 10
    except:
        # Запись вывода в переменную, с терминала, по запросу вывода информации хронящей нужные данные
        list_all_wifi = sp.check_output('sudo cat /data/misc/apexdata/com.android.wifi/WifiConfigStore.xml', shell=True)

        # Очистка лишнего и получения названия файлов, подключённых сетей
        list_all_wifi_pass = str(list_all_wifi).split(f'<string name="ConfigKey">&quot;{wifi_name}&quot;')[1]
        list_all_wifi_pass = str(list_all_wifi_pass).split(f'<int name="WEPTxKeyIndex" value="0" />')[0]
        if 'name="PreSharedKey">&quot;' in str(list_all_wifi_pass).split(f'<string name="SSID">&quot;{wifi_name}&quot;</string>')[1]:
            wifi_pass = str(list_all_wifi_pass).split('<string name="PreSharedKey">&quot;')[1]
            wifi_pass = str(wifi_pass).split('&quot;</string>')[0]
        elif 'name="PreSharedKey" />' in str(list_all_wifi_pass).split(f'<string name="SSID">&quot;{wifi_name}&quot;</string>')[1]:
            wifi_pass = 'Отсутствует'


    return wifi_pass



def main():
    # Список хронящий все имена и пароли wifi сетей
    list_wifi = []

    if platform.system() == 'Linux':
        if os.path.exists('/data/data'):
            # Цикл получения спика всех имён сетей, и их пароля
            for wifi_name in wifi_names():
                password = passwords(wifi_name)
                list_wifi.append([wifi_name, password])
    
    else: list_wifi.append('Упс, похоже что Вы запускаете не с Android!')

    return list_wifi



if __name__ == '__main__':
    main()
