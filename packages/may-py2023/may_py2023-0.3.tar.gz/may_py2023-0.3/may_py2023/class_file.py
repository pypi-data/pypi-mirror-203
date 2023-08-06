import json # Нужен для сохранения перемененных
import pathlib # Нужен для созданья папок
import shutil # Нужен для удаления папки
import os
from typing import Union # нужен для указания различных типов для переменной

# Если хотите использовать этот файл в других проектах и файлах, он не должен содержать вызовов

class File:

    # записать текст из 'text' в файл по пути 'path'(overwriting - вкл/выкл перезапись)
    @staticmethod
    def write_text(text: str, path: str, overwriting=True):
        # файл перезаписывается
        if overwriting:
            with open(path, mode='w') as file:
                file.write(text)
        # файл дополняется
        else:
            with open(path, mode='a+') as file:
                file.write(text)

    # читать текст из 'text' в файл по пути 'path'
    @staticmethod
    def read_text(path: str):
        with open(path, mode='r') as file:
            return file.read()

    # Записать словарь/список из 'data' в файл по пути 'path'
    @staticmethod
    def write_json(data: Union[dict, list], path: str):
        with open(path, mode='w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)

    # Прочитать словарь/список из файла по пути 'path'
    @staticmethod
    def read_json(path: str):
        with open(path, mode='r', encoding='utf8') as file:
            return json.load(file)

    #  Создание папки или всех папок в переданном пути. Указываем полный путь в 'path'
    @staticmethod
    def create_folder(path: str):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    # Удаление папок или всех данных в ней (будь это файлы или папки)
    @staticmethod
    def delete_folder(path: str):
        shutil.rmtree(path, ignore_errors=True)

    # Удаление файлов
    @staticmethod
    def delete_file(path: str):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass


