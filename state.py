from flask import Flask, jsonify

app = Flask(__name__)

# Different states for the traffic light
class RedState:
    def handle(self):
        return "Stop! The light is red."

class GreenState:
    def handle(self):
        return "Go! The light is green."

class YellowState:
    def handle(self):
        return "Caution! The light is yellow."

# Context (Traffic Light)
class TrafficLight:
    def __init__(self):
        self.state = RedState()

    def change_state(self, new_state):
        self.state = new_state

    def request(self):
        return self.state.handle()

traffic_light = TrafficLight()

@app.route('/traffic/<color>')
def change_light(color):
    if color == 'green':
        traffic_light.change_state(GreenState())
    elif color == 'yellow':
        traffic_light.change_state(YellowState())
    elif color == 'red':
        traffic_light.change_state(RedState())
    return jsonify(message=traffic_light.request())

if __name__ == "__main__":
    app.run(debug=True)
