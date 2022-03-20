# 4 Написать скрипт, который выводит статистику для заданной папки в виде словаря, в
# котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения —
# общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

dir_name = os.getcwd()
size1 = [item for item in os.listdir(dir_name) if os.stat(os.path.join(dir_name, item)).st_size <= 100]
size2 = [item for item in os.listdir(dir_name) if 100 < os.stat(os.path.join(dir_name, item)).st_size <= 1000]
size3 = [item for item in os.listdir(dir_name) if 1000 < os.stat(os.path.join(dir_name, item)).st_size <= 10000]
size4 = [item for item in os.listdir(dir_name) if 10000 < os.stat(os.path.join(dir_name, item)).st_size]
print({100: len(size1), 1000: len(size2), 10000: len(size3), 100000: len(size4)})