"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import os
import re
import csv

files_path = os.path.join(os.getcwd(), '')
txt = [os.path.join(files_path, file) for file in os.listdir(files_path) if re.findall(r'\.txt$', file)]


def get_data(files: list):
    head = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']
    line_data = [head]

    for file in files:
        with open(file, 'r') as file:
            file_data = file.read()

        data_row = list()
        for line in file_data.split('\n'):
            for header in head:
                row_item = re.findall(r'{}:\s+(.+)$'.format(header), line)
                if row_item:
                    data_row.append(row_item[0])

        line_data.append(data_row)

    return line_data


def write_csv(file, data_files):
    data = get_data(data_files)
    with open(file, 'w', encoding='utf-8') as data_report:
        writer = csv.writer(data_report)
        for row in data:
            writer.writerow(row)


write_csv('data_report.csv', txt)
