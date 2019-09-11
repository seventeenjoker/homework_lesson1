list = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]

for num in list:
    print(num + 1)

str1 = str(input('Введите строку:'))

for letter in str1:
    print(letter)

school_list = [
    {'school_class': '5a', 'scores': [4, 5, 3, 4, 4]},
    {'school_class': '5b', 'scores': [4, 2, 3, 4, 4]},
    {'school_class': '5c', 'scores': [4, 5, 1, 4, 4]},
    {'school_class': '6a', 'scores': [4, 5, 3, 5, 4]},
    {'school_class': '6b', 'scores': [4, 1, 3, 4, 4]},
    {'school_class': '6c', 'scores': [2, 5, 3, 4, 4]},
    {'school_class': '7a', 'scores': [4, 5, 3, 2, 1]}
]

# средний балл по классу и средний балл по школе
average = 0
average_school = 0
for dic in school_list:
    total = 0
    for value in dic['scores']:
        total +=value
    average = total / len(dic['scores'])
    print('Средний балл по классу {}: {}'.format(dic['school_class'], average))
    average_school += average
average_school = average_school / len(school_list)
print('Средний балл по школе: {}'.format(average_school))