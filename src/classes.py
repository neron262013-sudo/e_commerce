class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт"


    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = price

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(product_data["name"],
                   product_data["description"],
                   product_data["price"],
                   product_data["quantity"])


class Category:
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


    def __str__(self):
        all_products_quantity = 0
        for product in self.__products:
            all_products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {all_products_quantity} шт."


    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}.\n"
        return products_str

    @property
    def product_list(self):
        return self.__products


class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0


    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        if self.index < len(self.category.product_list):
            product = self.category.product_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
