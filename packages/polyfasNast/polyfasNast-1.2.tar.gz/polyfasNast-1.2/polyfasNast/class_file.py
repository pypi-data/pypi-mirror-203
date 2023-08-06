import json  # Нужен для сохранения переменных
import os
import pathlib  # Нужен для создания папок
import shutil  # Нужен для удаления папки
from typing import Union  # Нужен для указания различных типов для переменной

# Класс для работы с файлами и директориями
class File:

    # Записать текст из "text" в файл по пути "path" (overwriting - вкл/выкл перезапись)
    @staticmethod
    def write_text(text: str, path: str,overwriting=True):
        # Файл перезаписывается
        if overwriting:
            with open(path, mode="w") as file:
                file.write(text)
        # Файл дозаписывается (дополняется)
        else:
            with open(path, mode="a+") as file:
                file.write(text)

    # Читать текст из файла по пути "path"
    @staticmethod
    def read_text(path: str):
        with open(path, mode="r") as file:
            return file.read()

    # Записать словарь/список из "data" в файл по пути "path"
    @staticmethod
    def write_json(data: Union[dict, list], path: str):
        with open(path, mode="w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    # Прочитать словарь/список из "data" в файл по пути "path"
    @staticmethod
    def read_json(path: str):
        with open(path, mode="r", encoding='utf-8') as file:
            return json.load(file)

    # Создание папки или всех папок в переданном пути. Указываем полный путь в "path"
    @staticmethod
    def create_folder(path: str):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    # Удаление файла/папки или всех данных в ней (будь это файлы или папки).
    @staticmethod
    def delete_folder_or_file(path: str):
        shutil.rmtree(path, ignore_errors=True)

    # Удаление файла
    @staticmethod
    def delete_file(path: str):
        try:
            os.remove(path)  # У Игоря забрать остальное
        except:
            pass
        shutil.rmtree(path, ignore_errors=True)




