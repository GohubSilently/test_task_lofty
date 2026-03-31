class WeatherAPIError(Exception):
    pass


class CityNotFoundError(WeatherAPIError):
    pass


class InvalidAPIKeyError(WeatherAPIError):
    pass


class WeatherAPIUnavailable(WeatherAPIError):
    pass

class SubscriptionError(WeatherAPIError):
    pass
