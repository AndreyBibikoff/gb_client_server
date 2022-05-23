"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml


currency_icons = {'usa_dollar': '\u0024', 'euro': '\u20AC', 'russian_ruble': '\u20bd'}
exchange_rate = {'1\u0024': '73,70\u20bd', '1\u20AC': '87,02\u20bd'}
my_dict = {'exchange rate': exchange_rate, 'currency_icons': currency_icons}


with open('file.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml.safe_dump(my_dict, yaml_file, default_flow_style=False, allow_unicode=True)


print(my_dict)