"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json
import os
import re

files_path = os.path.join(os.getcwd(), '')

files_json = [os.path.join(files_path, file) for file in os.listdir(files_path) if re.findall(r'\.json$', file)]


def write_json(file, orders_data):
    with open(file, 'r') as json_file:
        data = json.load(json_file)

    data['orders'].append(orders_data)
    with open(file, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


new_order = {'item': 'Монитор LG 24MK430H 23.8', 'quantity': 5, 'price': 9490, 'buyer': 'Бибиков А. Л.', 'date': '26'
                                                                                                                 '.07'
                                                                                                                 '.2021'}

write_json(files_json[0], new_order)
