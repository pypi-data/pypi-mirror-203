#Тема 1. Работа с файлами")
import json # нужен для сохранения переменных
import pathlib # нужен для создания папок
import shutil # нужен для удаления папок
from typing import Union # нужен для указания различных типов для переменной
import os


# ---- Ш П А Р Г А Л К А ----
# r — открывает файл только для чтения.
# w — открывает файл только для записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для записи)
# w+ — открывает файл для чтения и записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для чтения и записи)
# a+ - открывает файл для чтения и записи.
#      (Информация добавляется в конец файла)
# b - открытие в двоичном режиме.

# Абсолютный путь (path) - показывает точное местонахождение файла
# Относительный путь (path) - показывает путь к файлу относительно какой-либо "отправной точки"

# JSON — текстовый формат обмена данными, основанный на JavaScript (похож на словарь или список Python)


# Класс для работы с файлами и директориями
class File:

    # Записать текст из "text" в файл по пути "path" (overwriteing - вкл/выкл перзапись)
    @staticmethod
    def write_text(text: str, path: str, overwriting=True):
        if overwriting:
            with open(path, mode="w") as file:
                file.write(text)
        else:
            with open(path, mode='a+') as file:
                file.write(text)

    # Читать текст из файла по пути "path"
    @staticmethod
    def read_text(path: str):
        with open(path, mode="r") as file:
            return file.read()

    # Записать словарь/список из "data" в файл по пути 'path'
    @staticmethod
    def write_json(data: Union[dict, list], path: str):
        with open(path, mode="w", encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)

    # Прочитать словарь/список из файла по пути 'path'
    @staticmethod
    def read_json(path: str):
        with open(path, mode="r", encoding='utf8') as file:
            return json.load(file)

    # Создание папки или всех папок в переданном пути. Указываем полный путь в "path"
    @staticmethod
    def create_folder(path: str):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    # Удаление папки и всех данных в ней. (будь это файлы или папки)
    @staticmethod
    def delete_folder(path: str):
        shutil.rmtree(path, ignore_errors=True)

    # Удаление файла

    @staticmethod
    def delete_file(path: str):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

# 1. пример использования методов write_text + read_text
# File.write_text("ABC", "text.txt")
# File.write_text("ABC", "text.txt", overwriting=False)
# File.write_text("ABC", "text.txt", overwriting=False)
# string = File.read_text("text.txt")
# print(string, type(string))
#
# # 2. пример использования методов write_text + read_text
# d = [{'name': 'Anya'}, {'name': 'Kostya', 'age': 22}, {'name1': 'Варфаламей', 'age': 26}, {'name': 'Baton', 'age': 37}]
# File.write_json(data=d, path='data.json')
#
# lst = File.read_json(path='data.json')
# print(lst[1]['name'], lst, type(lst))
# name = lst[1]['name']
# age = lst[1]['age']
# print('конкр элемент Json:', name, age)
#
# # 3. Пример создания папки 3 и всех предыдущих папок перед ней, если это необходимо
# File.create_folder(path=r'D:\Python311\PyProjects\Lesson06\1\2\3')
#
# # 4. Пример создания папки 2 и всех предыдущих папок перед ней, если это необходимо
# File.create_folder(path=r'D:\Python311\PyProjects\Lesson06\2')
#
# # 5. Пример удаления папки 2 и всех предыдущих папок перед ней, если это необходимо
# File.delete_folder(path=r'D:\Python311\PyProjects\Lesson06\1')
# File.delete_file(path=r'D:\Python311\PyProjects\Lesson06\2')
#
# # 6 Последовательная запись текста в один файл, True - перезапись включена, False - перезапись отключена
# # File.write_text(text="ABC", path="text.txt", overwriting=True)

