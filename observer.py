from flask import Flask, jsonify

app = Flask(__name__)

# Observer
class WeatherObserver:
    def update(self, weather_data):
        return f"Observer received update: {weather_data}"

# Subject (Weather Station)
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.weather_data = "Sunny"

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        updates = []
        for observer in self.observers:
            updates.append(observer.update(self.weather_data))
        return updates

    def set_weather(self, weather_data):
        self.weather_data = weather_data
        return self.notify_observers()

weather_station = WeatherStation()

@app.route('/subscribe')
def subscribe():
    observer = WeatherObserver()
    weather_station.add_observer(observer)
    return "Subscribed to weather updates!"

@app.route('/update_weather/<weather>')
def update_weather(weather):
    return jsonify(weather_station.set_weather(weather))

if __name__ == "__main__":
    app.run(debug=True)
