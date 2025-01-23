from pprint import pprint
import io


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}

    i = 0
    for string in strings:
        byte_position = file.tell()
        file.writelines(string+'\n')
        i += 1
        strings_positions[(i, byte_position)] = string

    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

