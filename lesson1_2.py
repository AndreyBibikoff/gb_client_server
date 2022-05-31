def str_to_bytes(user_str):
    b = eval("b" + user_str)
    print(b)
    print(type(b))
    print(len(b))


str_to_bytes("'class'")
str_to_bytes("'function'")
str_to_bytes("'method'")

