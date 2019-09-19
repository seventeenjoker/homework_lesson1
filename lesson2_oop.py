class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть не менее 3 символов.')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Скидка более 99%.')
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товаров на складе!')
        self.stock -= items_count
    
    def get_color(self):
        raise NotImplementedError

    def __repr__(self):
        return f'Product name: {self.name}, price: {self.price}, stock: {self.stock}'

class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color

    def get_color(self):
        return f'Цвет телефона: {self.color}'

    def get_memory(self):
        # Выводим размер памяти в гигабайтах
        pass

    def __repr__(self):
        return f'Phone name: {self.name}, price: {self.price}, stock: {self.stock}'

class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture

    def get_color(self):
        return f'Цвет софы: {self.color}'

    def __repr__(self):
        return f'Sofa name: {self.name}, price: {self.price}, stock: {self.stock}'

sofa1 = Sofa('Sofa_name', 30000, 'yellow', 'velure')
print(sofa1.get_color())

phone1 = Phone('iphone', 60000, 'black', 10)
print(phone1.get_color())