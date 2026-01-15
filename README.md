# Integral Calculations (Monte Carlo)

Небольшой инструмент для оценки двух интегралов с помощью Монте‑Карло. Есть простой middle-square генератор и вариант с NumPy RNG.

## Установка
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Использование
Запуск из командной строки:
```bash
python -m integral_calculations --n 5000 --method middle-square --seed 0.84616823
```
Параметры:
- `--n` — количество выборок (по умолчанию 5000)
- `--method` — `middle-square` или `numpy`
- `--seed` — seed (для middle-square должен быть в (0,1))
- `-k` — количество цифр для middle-square (чётное)

Пример вывода:
```
I1: 1.041233 (var=0.059812, stderr=0.003456)
I2: 1.983421 (var=0.192114, stderr=0.006192)
```

## API
- `middle_square_uniform(n, seed, k)` — псевдослучайные числа на [0,1).
- `sample_transforms(u)` — преобразования для двух демонстрационных интегралов.
- `estimate_integrals(...)` — возвращает оценки для I1/I2 с дисперсией и stderr.

## Тесты
```bash
pytest
```
