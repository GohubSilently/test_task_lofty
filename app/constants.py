from pathlib import Path

BASE_DIR = Path(__file__).parent

# Логирование
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "parser.log"
SIZE_LOG = 10**6
DT_FORMAT = "%d.%m.%Y %H:%M:%S"
LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"

START_HANDLER = "Обработчик запущен!"
END_HANDLER = "Обработчик завершил работу!"
COMMAND_LINE_ARGUMENTS = "Передаваемый город - {city}."
NOT_FOUND_DATA = 'Нет данных'

REQUEST_ERROR = 'Возникла ошибка при загрузке страницы {url} - {error}'

TIME_FOR_CACHE = 60 * 10  # 10 минут

WEATHER_CONDITION = {
    'Thunderstorm': 'Гроза',
    'Drizzle': 'Мелкий дождь',
    'Rain': 'Дождь',
    'Snow': 'Снег',
    'Clear': 'Ясно',
    'Clouds': 'Облачно',
    'Mist': 'Дымка',
    'Smoke': 'Смог',
    'Haze': 'Мгла',
    'Dust': 'Пыльно',
    'Ash': 'Пепел',
    'Squall': 'Шквал',
    'Tornado': 'Торнадо',
}
