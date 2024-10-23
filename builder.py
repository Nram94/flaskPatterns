from flask import Flask, jsonify

app = Flask(__name__)

class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_pizza(self):
        return f"Pizza with {', '.join(self.ingredients)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add_ingredient("cheese")
        return self

    def add_pepperoni(self):
        self.pizza.add_ingredient("pepperoni")
        return self

    def add_mushrooms(self):
        self.pizza.add_ingredient("mushrooms")
        return self

    def build(self):
        return self.pizza

@app.route('/')
def build_pizza():
    builder1 = PizzaBuilder()
    builder2 = PizzaBuilder()
    pizza1 = builder1.add_cheese().add_pepperoni().build()
    pizza2 = builder2.add_cheese().add_mushrooms().build()

    pizzas = [pizza1.get_pizza(),
              pizza2.get_pizza()]
    return pizzas

if __name__ == "__main__":
    app.run(debug=True)
