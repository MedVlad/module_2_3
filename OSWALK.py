import os
import time
import pathlib

currentDirectory = pathlib.Path('.')
for file in currentDirectory.iterdir():
        s = os.path.supports_unicode_filenames
        filepath = os.path.join(currentDirectory, os.path.abspath(file))
        if os.path.isfile(filepath):
            filesize = os.path.getsize(os.path.abspath(file))
            filetime = os.path.getmtime(filepath)
            formatted_time = time.ctime(filetime)
            parent_dir = filepath.split ('\\')[-2]
            y = os.path.dirname(filepath)

            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:{formatted_time} , Родительская директория: {parent_dir}')
