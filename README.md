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