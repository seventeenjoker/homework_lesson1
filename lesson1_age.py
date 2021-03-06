def what_to_do(age):
    if 0 < age < 6:
        return 'Учиться в детском саду'
    elif 6 <= age < 17:
        return 'Учиться в школе'
    elif 17 <= age < 23:
        return 'Учиться в ВУЗе'
    elif 23 <= age <= 120:
        return 'Работать'
    elif age <= 0 or age > 120:
        return 'Введен некорректный возраст'

for i in range(5):
    try:
        age = int(input('Введите свой возраст:'))
    except ValueError:
        if i == 4:
            print('Попытки определить чем вам заниматься закончены.')
            break
        print('Попробуйте снова.')
        continue
    task1 = what_to_do(age)
    print(task1)
    break