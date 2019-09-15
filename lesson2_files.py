# with open('myfile.txt', 'a', encoding = 'utf-8') as myfile:
    # myfile.write("\thello world!!!")

# with open('myfile.txt', 'r', encoding = 'utf-8') as myfile:
    # content = myfile.read()
    # print(content)

'''
Задание
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
'''

# with open('myfile.txt', 'r', encoding = 'utf-8') as myfile:
    #for line in myfile:
        #line = line.upper()
        #line = line.replace('\n', '')
        #print(line)

with open('referat.txt', 'r', encoding = 'utf-8') as myfile:
    content = myfile.read()
    len_content = len(content)
    list_words = content.split(' ')
    len_list_words = len(list_words)
    print(f'Длина файла: {len_content}.')
    print(f'Количество слов в тесте: {len_list_words}.')
    content = content.replace('.', '!')
    with open('referat2.txt', 'w', encoding = 'utf-8') as r2:
        r2.write(content)