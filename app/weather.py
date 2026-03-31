import logging

import requests_cache
from prettytable import PrettyTable

from configs import configure_logging, configure_parser
from constants import (
    COMMAND_LINE_ARGUMENTS,
    END_HANDLER,
    NOT_FOUND_DATA,
    TIME_FOR_CACHE,
    START_HANDLER,
    WEATHER_CONDITION
)
from exceptions import (
    CityNotFoundError,
    InvalidAPIKeyError,
    SubscriptionError,
    WeatherAPIUnavailable,
)
from utils import get_response


MAIN_URL = 'https://api.openweathermap.org/data/2.5/weather?'


def pretty_output(results):
    table = PrettyTable()
    table.field_names = results[0]
    table.add_rows(results[1:])
    print(table)


def output_weather(response):
    data = response.json()
    name = data['name']
    weather_condition = data['weather'][0]['main']
    temperature = data['main']['temp']
    return name, temperature, WEATHER_CONDITION[weather_condition]


def main():
    configure_logging()
    logging.info(START_HANDLER)
    parser = configure_parser()
    args = parser.parse_args()
    logging.info(COMMAND_LINE_ARGUMENTS.format(**vars(args)))

    session = requests_cache.CachedSession(expire_after=TIME_FOR_CACHE)
    if args.clear_cache:
        session.cache.clear()
    results = [('Город', 'Температура', 'Погодные условия')]
    for city in args.city:
        try:
            response = get_response(session, MAIN_URL, city)
            result = output_weather(response)
            if result is not None:
                results.append(result)
        except CityNotFoundError as error:
            logging.warning(error)
        except WeatherAPIUnavailable as error:
            logging.warning(error)
        except InvalidAPIKeyError as error:
            logging.warning(error)
        except SubscriptionError as error:
            logging.warning(error)
            return
    if len(results) != 1:
        pretty_output(results)
    else:
        logging.info(NOT_FOUND_DATA)

    logging.info(END_HANDLER)


if __name__ == '__main__':
    main()
