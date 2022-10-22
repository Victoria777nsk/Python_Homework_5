'''
Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''
with open('Text_for_RLE.txt', 'w', encoding = 'UTF-8') as file:    # Текстовый файл для входных данных от пользователя.
    file.write(input('Введите текст для сжатия: '))
with open('Text_for_RLE.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()
print(my_text)

def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:              # Проверяем, являются ли входные данные текстом.
        return ''

    for char in text:         # Перебираем все символы в тексте.
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding

text_compression = rle_encode(my_text)

with open('Text_compression_RLE_024.txt', 'w', encoding = 'UTF-8') as file:   # Текстовый файл для сжатого текста.
    file.write(f'{text_compression}')
print(text_compression)