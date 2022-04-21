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
            no_first_list.append('.'.join(ip[1:]))
        return no_first_list

    def last_only(self):
        last_only_list = []
        for elem in self.ips:
            ip = elem.split('.')
            last_only_list.append(ip[-1])
        return last_only_list


ip_adresses = ["10.11,12.13", "10a.11.12.14", "10.11.12.15"]
ip_proccessing = IpProccessing(ip_adresses)

# 1) Получить список IP адресов в развернутом виде
# (пример 10.11.12.13 -> 13.12.11.10)
print(ip_proccessing.revers())
# 2) Получить список IP адресов без первых октетов
# (пример 0.11.12.13 -> 11.12.13)
print(ip_proccessing.no_first())
# 3) Получить список последних октетов IP адресов
# (пример 10.11.12.13 -> 13)
print(ip_proccessing.last_only())


# I have made a cool "validator", but I cannot use it in the class element initiation, and I am a bit upset about it
# for elem in ["10.11.12.13", "10.11.12.a4", "10,11,12,15"]:
#     if elem.count('.') == 3 and all(i.isdigit() for i in elem.split('.')):
#         print("IP seems to be fine")
#     else:
#         print("Something wrong with your IP")


class FilesProccessing:
    """
    it gets the path and the mode as an input
    mode = a means add if file exist
    mode = w means re-write if file exist
    """

    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def write_it(self, text: str):
        if self.mode == 'w' or self.mode == 'a':
            text = str(text)  # I have checked; srt() can get RuntimeError or MemoryError only, so I don't need try/except
            with open(self.file_path, self.mode) as file:
                file.write(text + '\n')
        else:
            print(f"Entered mode {self.mode} is not 'w' or 'a'")
            return

    def eraste_it(self):
        with open(self.file_path, 'w') as file:
            return


files_processing = FilesProccessing('./test.txt', 'a')
files_processing.write_it('puppe1')
files_processing.eraste_it()
