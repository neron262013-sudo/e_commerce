from src.classes import Product


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
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_new_product_method(first_product_dict):
    product = Product.new_product(first_product_dict)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


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


def test_category_products_method(second_category):
    products = second_category.products
    assert products == "55\" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
