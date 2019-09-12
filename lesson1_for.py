list_ex = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]

for num in list_ex:
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
all_marks = [mark for class_info in school_list for mark in class_info['scores']]
school_sum = sum(all_marks)
school_avr = school_sum / len(all_marks)
print(f"Средний балл по школе: {school_avr}")

average_school = 0
for dic in school_list:
    average_class = sum(dic['scores']) / len(dic['scores'])
    print(f"Средний балл по классу {dic['school_class']}: {average_class}")