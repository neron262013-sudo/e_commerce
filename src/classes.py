class Product:
    # Создает объект класса Product из названия, описания, цены и количества
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    # Метод форматирования вывода информации о продукте print(str(product1))
    # Формат вывода "Название продукта, 80 руб. Остаток: 15 шт."
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт"


    # Метод сложения суммы двух продуктов с учетом их количества
    # Формула (цена прод1 * кол-во прод1 + цена прод2 * кол-во прод2)
    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity


    # Геттер price
    @property
    def price(self):
        return self.__price


    # Сеттер price. Если цена не 0 или отрицательная, то задаем цену. Иначе принтим предупреждение.
    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = price


    # Метод класса, создающий новый объект класса Product
    @classmethod
    def new_product(cls, product_data: dict):
        return cls(product_data["name"],
                   product_data["description"],
                   product_data["price"],
                   product_data["quantity"])


class Category:
    # Создает объект класса Category из названия, описания и списка продуктов
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)


    # Метод форматирования вывода информации о классе print(str(category1))
    # Формат вывода "Название категории, количество продуктов: 200 шт."
    def __str__(self):
        # Сначала считаем количество всех продуктов
        all_products_quantity = 0
        for product in self.__products:
            all_products_quantity += product.quantity
        # Затем, возвращаем сообщение
        return f"{self.name}, количество продуктов: {all_products_quantity} шт."


    # Добавляем продукт в список продуктов и увеличиваем счетчик количества продуктов
    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


    # Геттер списка товаров в текстовом виде
    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}.\n"
        return products_str


    # Геттер, в котором содержится сам список товаров (в виде list)
    @property
    def product_list(self):
        return self.__products


class CategoryIterator:
    # Итератор по списку товаров
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0


    # Получение итератора. Сбрасывает индекс списка на 0.
    def __iter__(self):
        self.index = 0
        return self


    # Получение следующего значения итератора из списка продуктов. Увеличивает индекс на 1.
    def __next__(self):
        if self.index < len(self.category.product_list):
            product = self.category.product_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
