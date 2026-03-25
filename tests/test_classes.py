import pytest

from src.classes import Product, Smartphone, LawnGrass


def test_product_init(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_price_setter(capsys, first_product):
    first_product.price = 200000.0
    assert first_product.price == 200000.0
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_new_product_method(first_product_dict):
    product = Product.new_product(first_product_dict)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str(first_product):
    assert str(first_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт"


def test_product_add(first_product, second_product):
    assert (first_product + second_product) == 2580000.0


def test_product_add_exception(first_product):
    with pytest.raises(TypeError):
        first_product + 1


def test_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")


def test_category_counters(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert len(first_category.product_list) == 3

    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                           "станет вашим другом и помощником")
    assert len(second_category.product_list) == 1

    assert first_category.category_count == 2
    assert first_category.product_count == 4

    assert second_category.category_count == 2
    assert second_category.product_count == 4


def test_category_add_product_method(first_category, second_product):
    first_category.add_product(second_product)
    assert second_product in first_category.product_list
    assert first_category.product_count == 4


def test_dd_product_add_product_exception(first_category):
    with pytest.raises(TypeError):
        first_category + 1


def test_category_products_method(second_category):
    products = second_category.products
    assert products == "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."


def test_category_iter(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator).name == "Iphone 15"
    assert next(category_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(category_iterator)


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_smartphone_add(first_smartphone, second_smartphone):
    assert first_smartphone + second_smartphone == 2580000.0


def test_smartphone_add_exception(first_smartphone, first_lawn_grass):
    with pytest.raises(TypeError):
        first_smartphone + 1
    with pytest.raises(TypeError):
        first_smartphone + first_lawn_grass


def test_lawn_grass_init(first_lawn_grass):
    assert first_lawn_grass.name == "Газонная трава"
    assert first_lawn_grass.description == "Элитная трава для газона"
    assert first_lawn_grass.price == 500.0
    assert first_lawn_grass.quantity == 20
    assert first_lawn_grass.country == "Россия"
    assert first_lawn_grass.germination_period == "7 дней"
    assert first_lawn_grass.color == "Зеленый"


def test_lawn_grass_add(first_lawn_grass, second_lawn_grass):
    assert first_lawn_grass + second_lawn_grass == 16750.0


def test_lawn_grass_add_exception(first_lawn_grass, first_smartphone):
    with pytest.raises(TypeError):
        first_lawn_grass + 1
    with pytest.raises(TypeError):
        first_lawn_grass + first_smartphone



def test_mixin_info_print(capsys):
    Product(name="Samsung Galaxy S23 Ultra",
            description="256GB, Серый цвет, 200MP камера",
            price=180000.0,
            quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product, 256GB, Серый цвет, 200MP камера, 180000.0, 5"

    Smartphone("Samsung Galaxy S23 Ultra",
               "256GB, Серый цвет, 200MP камера",
               180000.0,
               5,
               95.5,
               "S23 Ultra",
               256,
               "Серый")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone, 256GB, Серый цвет, 200MP камера, 180000.0, 5"

    LawnGrass("Газонная трава",
              "Элитная трава для газона",
              500.0,
              20,
              "Россия",
              "7 дней",
              "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass, Элитная трава для газона, 500.0, 20"
