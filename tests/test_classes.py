def test_product_init(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")


def test_category_counters(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получения дополнительных функций для удобства жизни")
    assert len(first_category.products) == 3

    assert second_category.name == "Телевизоры"
    assert second_category.description == ("Современный телевизор, который позволяет наслаждаться просмотром, "
                                           "станет вашим другом и помощником")
    assert len(second_category.products) == 1

    assert first_category.category_count == 2
    assert first_category.product_count == 4

    assert second_category.category_count == 2
    assert second_category.product_count == 4
