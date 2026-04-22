from datetime import datetime


def get_time_greeting() -> str:
    """Получение строки приветствия"""

    time = datetime.now().time()

    if 5 <= time.hour < 10:
        greeting = "Доброе утро!"
    elif 10 <= time.hour < 17:
        greeting = "Добрый день!"
    elif 17 <= time.hour < 22:
        greeting = "Добрый вечер!"
    else:
        greeting = "Доброй ночи!"

    return greeting
