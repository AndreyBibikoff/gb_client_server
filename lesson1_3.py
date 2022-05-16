def str_to_bytes(user_str):
    try:
        b = eval("b" + user_str)
        print(b)
    except SyntaxError: print(f'Слово {user_str} невозможно записать в байтовом типе')


str_to_bytes("'attribute'")
str_to_bytes("'класс'")
str_to_bytes("'функция'")
str_to_bytes("'type'")

