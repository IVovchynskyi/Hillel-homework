"""
# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов в развернутом виде
# (пример 10.11.12.13 -> 13.12.11.10)
# 2) Получить список IP адресов без первых октетов
# (пример 0.11.12.13 -> 11.12.13)
# 3) Получить список последних октетов IP адресов
# (пример 10.11.12.13 -> 13)

Пример инициализации класса
ip_adresses = ["10.11.12.13", "10.11.12.14", "10.11.12.15"]
ip_proccessing = IpProccessing(ip_adresses)

# Задача-2
# Вам необходимо написать
# класс который будет описывать работу с файлами, а
# именно:
# 1) Запись данных в файл
# 2) Чтение данных из файла
# 3) Удаление данных из файла

Пример
files_processing = FilesProccessing(file_path, mode)
"""

class IpProccessing:
    """
    list of IP addresses to be processed in various ways
    """
    def __init__(self, ips):
       self.ips = ips

    def revers(self):
        revers_list = []
        for elem in self.ips:
            ip = elem.split('.')
            revers_list.append('.'.join(ip[::-1]))
        return revers_list

    def no_first(self):
        no_first_list = []
        for elem in self.ips:
            ip = elem.split('.')
            no_first_list.append('.'.join(ip[1::]))
        return no_first_list


ip_adresses = ["10.11.12.13", "10.11.12.14", "10.11.12.15"]
ip_proccessing = IpProccessing(ip_adresses)

# 1) Получить список IP адресов в развернутом виде
# (пример 10.11.12.13 -> 13.12.11.10)
print(ip_proccessing.revers())
# 2) Получить список IP адресов без первых октетов
# (пример 0.11.12.13 -> 11.12.13)
print(ip_proccessing.no_first())