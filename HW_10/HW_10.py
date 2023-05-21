class Flower:  # Создание класса Цветок со временем увядания

    def __init__(self, name, freshness, length, color, price):
        self.name = name
        self.freshness = freshness
        self.length = length
        self.color = color
        self.price = price

    def get_wilt_time(self):
        if self.name == "Роза":
            return 5
        elif self.name == "Тюльпан":
            return 3
        elif self.name == "Гвоздика":
            return 4
        else:
            return 0

    def __str__(self):
        return f"{self.name} ({self.color}, {self.length} см., " f"{self.price} руб.)"


class Accessory:  # Создание класса Аксессуар с параметрами имени и цены

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price} руб)"


class Bouquet:  # Создание класса "Букет"

    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def get_cost(self):
        return sum(flower.price for flower in self.flowers) + sum(
            accessory.price for accessory in self.accessories
        )

    def get_wilt_time(self):
        return sum([flower.get_wilt_time() for flower in self.flowers]) / len(
            self.flowers
        )

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def has_flower(self, flower):
        return flower in self.flowers


# ------------------создание экземпляра класса-----------------------------

# Создаем несколько цветов для проверки, экземпляру класса присвоили переменные
rose = Flower("Роза", 4, 49, "Красный", 99)
tulip = Flower("Тюльпан", 2, 29, "Желтый", 49)
carnation = Flower("Гвоздика", 3, 39, "Розовый", 69)

# Создаем несколько аксессуаров для проверки
ribbon = Accessory("Лента", 19)
wrapper = Accessory("Обертка", 29)

# Создаем букет и добавляем в него цветы и аксессуары
bouquet = Bouquet()  # присвоили классу переменную для последующего вызова методов
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(carnation)
bouquet.add_accessory(ribbon)
bouquet.add_accessory(wrapper)

# --------------------------выполнение проверки ------------------------------------------

# Вычисляем стоимость букета
print("Стоимость букета:", bouquet.get_cost())

# Вычисляем время увядания букета
print("Время увядания букета:", bouquet.get_wilt_time())

# Сортируем цветы в букете по стоимости
bouquet.sort_by_price()
print("Цветы в букете, отсортированные по стоимости:")
for flower in bouquet.flowers:
    print(flower)

# Проверяем, есть ли цветок в букете
print("Цветок 'Роза' в букете:", bouquet.has_flower(rose))
print("Цветок 'Хризантема' в букете:", bouquet.has_flower(Flower))