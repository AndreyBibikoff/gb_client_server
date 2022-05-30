import chardet


file_string = ['сетевое программирование', 'сокет', 'декоратор']


with open('test_file.txt', 'w') as f:
    for i in file_string:
        f.write(i + '\n')
    f.close()

enc = ''

with open('test_file.txt', 'rb') as f:
    for i in f:
        enc = chardet.detect(i)
    f.close()

print(enc['encoding'])

with open('test_file.txt', 'r', encoding=enc['encoding']) as f:
    for i in f:
        print(i)
    f.close()