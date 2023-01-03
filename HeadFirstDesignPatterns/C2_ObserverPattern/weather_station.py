from observer_pattern import Subject, Observer, DisplayElement


class WeatherData(Subject):
    __temperature = None
    __humidity = None
    __pressure = None

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurements_changed()

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity

    @property
    def pressure(self):
        return self.__pressure


class CurrentConditionsDisplay(Observer, DisplayElement):
    __temperature = None
    __humidity = None

    def __init__(self, weather_data):
        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, obs, *args):
        if isinstance(obs, WeatherData):
            self.__temperature = obs.temperature
            self.__humidity = obs.humidity
            self.display()

    def display(self):
        print(f'Current conditions: {self.__temperature}F degrees and {self.__humidity}% humidity')


class StatisticsDisplay(Observer, DisplayElement):
    __max_temp = 0
    __min_temp = 200
    __temp_sum = 0
    __num_readings = 0

    def __init__(self, weather_data):
        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, obs, *args):
        if isinstance(obs, WeatherData):
            self.__temp_sum += obs.temperature
            self.__num_readings += 1

            if obs.temperature > self.__max_temp:
                self.__max_temp = obs.temperature
            if obs.temperature < self.__min_temp:
                self.__min_temp = obs.temperature

            self.display()

    def display(self):
        print(f'Avg/Max/Min temperature = {(self.__temp_sum / self.__num_readings)}/{self.__max_temp}/{self.__min_temp}')


class ForecastDisplay(Observer, DisplayElement):
    __current_pressure = 29.92
    __last_pressure = None

    def __init__(self, weather_data):
        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, obs, *args):
        if isinstance(obs, WeatherData):
            self.__last_pressure = self.__current_pressure
            self.__current_pressure = obs.pressure
            self.display()

    def display(self):
        print('Forecast: ', end='')
        if self.__current_pressure > self.__last_pressure:
            print('Improving weather on the way!')
        elif self.__current_pressure == self.__last_pressure:
            print('More of the same')
        elif self.__current_pressure < self.__last_pressure:
            print('Watch out for cooler, rainy weather')


class HeatIndexDisplay(Observer, DisplayElement):
    __heat_index = 0

    def __init__(self, weather_data):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, obs, *args):
        if isinstance(obs, WeatherData):
            self.__heat_index = self.__compute_heat_index(
                obs.temperature,
                obs.humidity
            )
            self.display()

    def display(self):
        print(f'Heat index is {self.__heat_index:.2f}')

    def __compute_heat_index(self, t, rh):
        return (
                (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh)
                 + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh))
                 + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
                 (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *
                 (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) +
                 (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
                 0.000000000843296 * (t * t * rh * rh * rh)) -
                (0.0000000000481975 * (t * t * t * rh * rh * rh))
        )


if __name__ == '__main__':
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    heat_index_display = HeatIndexDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
