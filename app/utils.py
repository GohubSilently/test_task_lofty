import os

from dotenv import load_dotenv
from requests import RequestException

from constants import REQUEST_ERROR
from exceptions import (
    CityNotFoundError,
    InvalidAPIKeyError,
    SubscriptionError,
    WeatherAPIError,
    WeatherAPIUnavailable,
)


load_dotenv()


API_KEY = os.getenv('API_KEY')


def get_response(session, url, city):
    if not API_KEY:
        raise InvalidAPIKeyError('Проверьте наличие API_KEY в .env')

    try:
        response = session.get(
            url,
            params={
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            },
            timeout=15
        )
    except RequestException as error:
        raise WeatherAPIUnavailable(
            REQUEST_ERROR.format(url=url, error=error)
        )
    if response.status_code == 400000:
        raise SubscriptionError(f'Проверьте подписку!')
    if response.status_code == 401:
        raise InvalidAPIKeyError(f'Проблема с API ключом!')
    if response.status_code == 404:
        raise CityNotFoundError(f'Город {city} не найден!')
    if response.status_code == 429:
        raise WeatherAPIUnavailable(f'Слишком много запросов!')
    if response.status_code >= 500:
        raise WeatherAPIUnavailable(f'Обратитесь в поддержку OpenWeather!')
    if response.status_code == 200:
        return response
    else:
        raise WeatherAPIError('Ошибка!')
