# unit-tests-lab-4

- **Студент:** Генчева Олена
- **Група:** З-41
- **Номер журналу:** 9
- **Варіант:** 9
- **Мова:** Python (PyTest)
- **Функція:** `loyalty_points(amount, is_member)`

## Правило
Функція повертає кількість балів лояльності.
1 бал за кожні повні 20 грн суми покупки.
Якщо покупець — учасник програми (`is_member = True`), бали подвоюються.
Якщо `amount < 0` — це помилка (`ValueError`), а не 0 балів.

## Запуск
    pip install pytest pytest-cov
    python -m pytest
    python -m pytest --cov=loyalty --cov-report=term-missing

## Покриття
100 % рядків модуля `loyalty.py` (7 passed).
