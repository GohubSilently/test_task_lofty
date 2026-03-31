# Тестовое задание для Lofty

[![Python](https://img.shields.io/badge/-Python_3.13-3771a1?style=flat&logo=Python&logoColor=ffffff)](https://www.python.org/)

Автор - [Халин Вадим](https://t.me/gohub1)

---

## Оглавление:
- [Описание](#описание)
- [Структура проекта](#структура-проекта)
- [Технологии](#технологии)
- [Локальный запуск](#локальный-запуск)

---

## Описание:
Небольшой CLI-скрипт для получения текущей погоды по названию города через OpenWeatherMap API.
Программа принимает один или несколько городов из командной строки и выводит температуру и погодные условия в виде таблицы.

---

## Структура проекта:
```text
├── app
│   ├── logs  # Созщдается при первом запуске
│   │   └── parser.log
│   ├── __init__.py
│   ├── configs.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── utils.py
│   └── weather.py
├── .env.example
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock

```

## Технологии:
- Python
- OpenWeatherAPI

---

## Локальный запуск:
1. Клонируем репозиторий.
```
git clone git@github.com:GohubSilently/test_task_lofty.git
cd test_task_lofty && cd app
```

2. Создаем .env.
```
API_KEY = your_api_key
```

3. Запускаем скрипт.
```
uv run weather.py Mocsow
```

[!Photo](https://github.com/GohubSilently/test_task_lofty/blob/main/Снимок%20экрана%202026-03-31%20в%2022.33.34.png)

[!Photo](https://github.com/GohubSilently/test_task_lofty/blob/main/Снимок%20экрана%202026-03-31%20в%2022.33.55.png)

---
