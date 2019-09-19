'''
Задание
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
'''

with open('referat.txt', 'r', encoding = 'utf-8') as myfile:
    content = myfile.read()
    len_content = len(content)
    list_words = content.split()
    len_list_words = len(list_words)
print(f'Длина файла: {len_content}.')
print(f'Количество слов в тесте: {len_list_words}.')
content = content.replace('.', '!')
with open('referat2.txt', 'w', encoding = 'utf-8') as r2:
    r2.write(content)