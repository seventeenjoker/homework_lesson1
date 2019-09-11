def discounted(price, discount):
    try:
        price_with_discount = price - (price * discount / 100)
        print(price_with_discount)
    except TypeError:
        print('Программа принимает на вход только числа.')

discounted(10000.0, 5)