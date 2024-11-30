import os
import time

directory = "."
for root, dirs, files in os.walk(directory):
  for file in files: # Перебираем все файлы
    filepath = os.path.join(rf'{root}\{file}')  # Путь к файлу, с полным указанием пути
    filetime = os.path.getmtime(rf'{root}\{file}') # Время последнего изменения файла
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # Формат записи времени
    filesize = os.path.getsize(rf'{root}\{file}') # Размер файла в байтах
    parent_dir = os.path.dirname(os.path.abspath(rf'{root}\{file}'))  # Родительская директория файла
    if parent_dir == os.path.dirname(os.path.abspath(file)): # выводим на печать обнаруженные в директории файлы
      print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')