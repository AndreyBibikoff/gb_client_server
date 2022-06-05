"""Программа-сервер"""

import socket
import sys
import json
from common.var import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message
import logging
import logs.config_server_log
from errors import IncorrectDataRecivedError

SERVER_LOGGER = logging.getLogger('server')


def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    SERVER_LOGGER.debug(f'Cообщениe от клиента : {message}')

    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'User':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.1.2
    :return:
    '''

    if '-p' in sys.argv:
        listen_port = int(sys.argv[sys.argv.index('-p') + 1])
    else:
        listen_port = DEFAULT_PORT
    if listen_port < 1024 or listen_port > 65535:
        SERVER_LOGGER.critical(f'Неподходящий порт для запуска - {listen_port}. Допустимы адреса с 1024 до 65535.')
        sys.exit(1)

    if '-a' in sys.argv:
        listen_address = sys.argv[sys.argv.index('-a') + 1]
        SERVER_LOGGER.info(f'Запущен сервер с параметрами подключения {listen_address}:{listen_port}')
    else:
        listen_address = ''
    SERVER_LOGGER.info(f'Запущен сервер с параметрами подключения: Все сетевые интерфейсы, порт: {listen_port}')

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        SERVER_LOGGER.info(f'Установлено соедение с {client_address}')
        try:
            message_from_cient = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение {message_from_cient}')
            response = process_client_message(message_from_cient)
            SERVER_LOGGER.info(f'Отправлен ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Закрывается соединение с {client_address}')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать JSON строку, полученную от '
                                f'клиента {client_address}. Соединение закрывается.')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_address} приняты некорректные данные. '
                                f'Соединение закрывается.')
            client.close()


if __name__ == '__main__':
    main()
