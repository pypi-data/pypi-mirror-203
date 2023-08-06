import requests

url_city = f"http://api.openweathermap.org/data/2.5/forecast?q=Valencia&appid=30327208ce508bd9097832f10c756ab9&units=metric"
url_loc = f"http://api.openweathermap.org/data/2.5/forecast?lat=40.1&lon=3.4&appid=30327208ce508bd9097832f10c756ab9"


class Weather:
    """Creates a Weather object getting an apiKey as input
    and either a city name or lat and lon coordinates.

    Package use example:

    ## Create a weather object using a city name:
    ## The apiKey below is not guaranteed to work.
    ## Request your own apiKey from https://openweathermap.org
    ## and wait for apiKey activation.

    >>> weather1 = Weather(apiKey='30327208ce508bd9097832f10c756ab9', city='Zagreb')

    ## Using latitude and longitude coordinates
    >>> weather2 = Weather(apiKey='30327208ce508bd9097832f10c756ab9', lat=41.1, lon=-4.1)

    ## Get complete weather data for the next 12 hours
    >>> weather1.next_12h()

    ## Simplified data for the next 12 hours
    >>> weather1.next_12h_simplified()

    Sample url to get sky condition icons:
    https://openweathermap.org/img/wn/10d@2x.png
    """

    def __init__(self, apiKey, city=None, lat=None, lon=None):

        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units=metric"
            r = requests.get(url)
            self.data = r.json()

        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apiKey}&units=metric"
            r = requests.get(url)
            self.data = r.json()

        else:
            raise TypeError(
                "Provide either a city name or lat & lon arguments")

        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        """Returns 3-hour data for next 12 hours as a dict.
        """
        return self.data["list"][:4]

    def next_12h_simplified(self):
        """Returns date, temperature, and sky condition every 3 hours
            for the next 12 hours as a list of tuples
        """
        simple_data = []
        for d in self.next_12h():
            simple_data.append(
                (
                    d["dt_txt"],
                    f'{d["main"]["temp"]} °C',
                    d["weather"][0]["description"].capitalize(),
                    d["weather"][0]["icon"]
                )
            )
        return simple_data
