# Проект "e-commerce"

## Описание
Тестовый проект для обучения

## Установка

1. Клонируйте репозиторий.
```
git clone https://github.com/neron262013-sudo/e_commerce
```
2. Установите зависимости.
```
pip install -r requirements.txt
```

## Список зависимостей
- black==26.3.1
- click==8.3.1
- colorama==0.4.6
- coverage==7.13.4
- flake8==7.3.0
- iniconfig==2.3.0
- isort==8.0.1
- librt==0.8.1
- mccabe==0.7.0
- mypy==1.19.1
- mypy_extensions==1.1.0
- packaging==26.0
- pathspec==1.0.4
- platformdirs==4.9.4
- pluggy==1.6.0
- pycodestyle==2.14.0
- pyflakes==3.4.0
- Pygments==2.19.2
- pytest==9.0.2
- pytest-cov==7.0.0
- pytokens==0.4.1
- typing_extensions==4.15.0


## Использование
1. Создать объект из класса Product. (classes.py)
```
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
```

2. Создать объект из класса Category. (classes.py)
```
category1 = Category("Смартфоны",
                     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                     [product1, product2, product3])
```
3. Создать объект из класса CategoryIterator. (classes.py)
```
my_iterator = CategoryIterator(category1)
```
## Класс Product.

Код для примера работы функционала в разделе "Код для примера работы"

2. self метод price устанавливает цену если она больше 0

```
new_product.price = 800
print(new_product.price)
new_product.price = -100
print(new_product.price)
new_product.price = 0
print(new_product.price)
```

3. cls метод new_product добавляет новый продукт из словаря

```
new_product = Product.new_product({"name": "Samsung Galaxy S23 Ultra",
                                   "description": "256GB, Серый цвет,200MP камера",
                                   "price": 180000.0,
                                   "quantity": 5
                                   })
```

4. __str__ метод выводит описание продукта в формате "Название продукта, 80 руб. Остаток: 15 шт"

```
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

print(str(product2))
```

5. __add__ метод складывает общую сумму всего количества двух продуктов
```
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

print(product2 + product3)
```

## Класс Category.

Код для примера работы функционала в разделе "Код для примера работы"

1. Метод add_product добавляет продукт класса Product в список продуктов и увеличивает счетчик продуктов на 1

```
product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
category1.add_product(product4)
```

2. Геттер products выводит список продуктов в консоль

```
print(category1.products)
```

3. __str__ метод выводит описание категории в формате "Название категории, количество продуктов: 200 шт."
```
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3]
)

print(str(category1))
```

## Класс CategoryIterator

Код для примера работы функционала в разделе "Код для примера работы"

1. __iter__ метод устанавливает счетчик индекса на 0

2. __next__ метод перебирает продукты из категории.
```
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3]
)

my_iterator = CategoryIterator(category1)

for product in my_iterator:
    print(product)
```
## Код для примера работы

Код нужно расположить в файле main.py в корневой директории

```
from src.classes import Product, Category, CategoryIterator

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
    
    print(str(product1))
    print(str(product2))
    print(str(product3))
    
    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
    
    my_iterator = CategoryIterator(category1)

    for product in my_iterator:
        print(product)
```

## Тестирование

Тестирование через pytest
1. Установите pytest и pytest-cov
```
poetry add --dev pytest pytest-cov
```
2. Запустите pytest и pytest-cov
```
pytest
pytest -cov
```
Используется файл tests\conftest.py для конфигурации тестирования.