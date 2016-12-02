# Price format
Данный скрипт конвертирует цену в удобный для чтения формат. 

## Запуск скрипта
Доступны 2 способа использовать скрипт:

1) прямое использование. Для этого запустите в консоли:
```bash
python3 format_price.py price
```
2) импорт функции:
```python
from format_price import format_price
print(format_price(price))
```

### Тесты
Для проверки корректной работы скрипта доступен файл tests.py, который достаточно просто запустить так:
```bash
python3 tests.py
```
Будет выдана информация о количестве запущенных тестов и их результатах.