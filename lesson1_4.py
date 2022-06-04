def str_to_bytes(user_str):
    b = user_str.encode(encoding='utf-8')
    print(b)
    print(type(b))
    s = b.decode(encoding='utf-8')
    print(s)
    print(type(s))

str_to_bytes('разработка')
str_to_bytes("администрирование")
str_to_bytes("protocol")
str_to_bytes("standard")