""" FileNotFoundError"""
import os
file_name = "example1.txt"
# Знаходимо адресу даного файлу
curr_path = os.path.abspath(__file__)
# Адреса на одну директорію вище
dir_path = os.path.dirname(curr_path)
# Створюємо локальну адресу файлу
file_path = os.path.join(dir_path, file_name)

try:
    file = open(file_path)
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
