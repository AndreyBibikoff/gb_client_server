
import os
import re
import csv

import chardet

files_path = os.path.join(os.getcwd(), '')
txt = [os.path.join(files_path, file) for file in os.listdir(files_path) if re.findall(r'\.txt$', file)]


def get_data(files: list):
    head = ['Название ОС', 'Код продукта', 'Изготовитель системы', 'Тип системы']
    line_data = [head]

    for file in files:
        with open(file, 'rb') as file:
            file_bytes = file.read()
            result = chardet.detect(file_bytes)
            data = file_bytes.decode(result['encoding'])

        data_row = list()
        for line in data.split('\n'):
            for header in head:
                if header == 'Название ОС':
                    row_item_os = re.findall(r'Windows\s\S'.format(header), line)
                    if row_item_os:
                        data_row.append(str(row_item_os[0]))
                else:
                    row_item = re.findall(r'{}:\s*\S*'.format(header), line)
                    if row_item:
                        data_row.append(str(row_item[0]).split()[-1])

        line_data.append(data_row)

    return line_data


def write_csv(file, data_files):
    data = get_data(data_files)
    with open(file, 'w', encoding='utf-8') as data_report:
        writer = csv.writer(data_report)
        for row in data:
            writer.writerow(row)


write_csv('data_report.csv', txt)
