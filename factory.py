from flask import Flask, jsonify

app = Flask(__name__)

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        return None

@app.route('/animal/<animal_type>')
def get_animal(animal_type):
    animal = AnimalFactory.get_animal(animal_type)
    if animal:
        return jsonify(speak=animal.speak())
    else:
        return jsonify(error="Unknown animal type"), 404

if __name__ == "__main__":
    app.run(debug=True)
