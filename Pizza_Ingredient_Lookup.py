from abc import ABC, abstractmethod
import time


def ListToStr(any):
    str1 = ", "
    return (str1.join(any))


# Factory
class Pizza(ABC):
    @abstractmethod
    def get_ingredient(self):
        pass


# Pizzas
class Vesuvio(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham"]

    def get_ingredient(self):
        return self.ingredients


class Cacciatore(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham"]

    def get_ingredient(self):
        return self.ingredients


class Pescatore(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Tuna"]

    def get_ingredient(self):
        return self.ingredients


class Marinara(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Mussels", "Shrimps"]

    def get_ingredient(self):
        return self.ingredients


class Tomaso(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham", "Shrimps"]

    def get_ingredient(self):
        return self.ingredients


class Peperone(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Paprika", "Olives"]

    def get_ingredient(self):
        return self.ingredients


class Margherita(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese"]

    def get_ingredient(self):
        return self.ingredients


class Capricciosa(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham", "Mushrooms"]

    def get_ingredient(self):
        return self.ingredients


class Calzone(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham"]

    def get_ingredient(self):
        return self.ingredients

class Riviera(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Tuna", "Shrimps"]

    def get_ingredient(self):
        return self.ingredients


class Lamaffia(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Bacon", "Onions", "Cayenne pepper"]

    def get_ingredient(self):
        return self.ingredients


class Mamamia(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ground beef"]

    def get_ingredient(self):
        return self.ingredients


class Pranzo(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Bacon", "Egg"]

    def get_ingredient(self):
        return self.ingredients


class Dennisso(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Mushrooms", "Shrimps"]

    def get_ingredient(self):
        return self.ingredients


class Hawaii(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham", "Pineapple"]

    def get_ingredient(self):
        return self.ingredients


class Vegetariana(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Mushrooms", "Olives", "Paprika", "Onions"]

    def get_ingredient(self):
        return self.ingredients


class Bambino(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham", "Mushrooms", "Pineapples"]

    def get_ingredient(self):
        return self.ingredients


class Bari(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Ham", "Tuna"]

    def get_ingredient(self):
        return self.ingredients


class Africana(Pizza):
    def __init__(self):
        self.ingredients = ["Tomato", "Cheese", "Banana", "Pineapples", "Curry"]

    def get_ingredient(self):
        return self.ingredients


pizzas = ["vesuvio", "cacciatore", "pescatore", "marinara", "tomaso", "peperone", "margherita", "capricciosa",
          "calzone", "riviera", "lamaffia", "mamamia", "pranzo", "dennisso", "hawaii", "vegetariana", "bambino", "bari",
          "africana"]


class PizzaOrder:
    @staticmethod
    def get_pizza(PizzaType: str):
        PizzaToCall = eval(PizzaType.capitalize() + "()")
        return PizzaToCall


def pizza_run_gui(input_order):
    if input_order.lower() in pizzas:
        order = PizzaOrder.get_pizza(input_order)
        return True, ListToStr(order.get_ingredient())
    else:
        return False, "That pizza is not on our menu!"
