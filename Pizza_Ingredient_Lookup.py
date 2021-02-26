from abc import ABC, abstractmethod
import time

def ListToStr(any):  
    str1 = ", " 
    return (str1.join(any)) 

#Factory
class Pizza(ABC):
    @abstractmethod
    def get_ingredient(self):
        pass

#Pizzas
class Vesuvio(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Skinka"]
    def get_ingredient(self):
        return self.ingredients
class Cacciatore(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Salami"]     
    def get_ingredient(self):
        return self.ingredients
class Pescatore(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Tonfisk"]     
    def get_ingredient(self):
        return self.ingredients
class Marinara(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Musslor", "Räkor"]     
    def get_ingredient(self):
        return self.ingredients
class Tomaso(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Skinka", "Räkor"]     
    def get_ingredient(self):
        return self.ingredients
class Peperone(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Paprika", "Oliver"]     
    def get_ingredient(self):
        return self.ingredients
class Margherita(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost"]     
    def get_ingredient(self):
        return self.ingredients
class Capricciosa(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Skinka", "Champinjoner"]     
    def get_ingredient(self):
        return self.ingredients
class Calzone(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Skinka"]
        self.inbakad = True    
    def get_ingredient(self):
        return self.ingredients, self.inbakad
class Riviera(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Tonfisk", "Räkor"]     
    def get_ingredient(self):
        return self.ingredients
class Lamaffia(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Bacon", "Lök", "Cayennepeppar"]     
    def get_ingredient(self):
        return self.ingredients
class Mamamia(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Köttfärs"]     
    def get_ingredient(self):
        return self.ingredients
class Pranzo(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Bacon", "Ägg"]     
    def get_ingredient(self):
        return self.ingredients
class Dennisso(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Champinjoner", "Räkor"]     
    def get_ingredient(self):
        return self.ingredients
class Hawaii(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Skinka", "Ananas"]     
    def get_ingredient(self):
        return self.ingredients
class Vegetariana(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Champinjoner", "Oliver", "Paprika", "Lök"]     
    def get_ingredient(self):
        return self.ingredients
class Bambino(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Skinka", "Champinjoner", "Ananas"]     
    def get_ingredient(self):
        return self.ingredients
class Bari(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Skinka", "Tonfisk"]     
    def get_ingredient(self):
        return self.ingredients
class Africana(Pizza):
    def __init__(self):
        self.ingredients = ["Tomat", "Ost", "Banan", "Ananas", "Curry"]     
    def get_ingredient(self):
        return self.ingredients

pizzas = ["vesuvio", "cacciatore", "pescatore", "marinara", "tomaso", "peperone", "margherita", "capricciosa", "calzone", "riviera", "lamaffia", "mamamia", "pranzo", "dennisso", "hawaii", "vegetariana", "bambino", "bari", "africana"]

class PizzaOrder:
    @staticmethod
    def get_pizza(PizzaType: str):
        PizzaToCall = eval(PizzaType.capitalize() + "()")
        return PizzaToCall


def pizza_run_gui(input_order):
    if input_order.lower() in pizzas:
        order = PizzaOrder.get_pizza(input_order)
        print("This pizza contains the following ingredients: {}".format(ListToStr(order.get_ingredient())))
        return ListToStr(order.get_ingredient())
    else:
        print("Pizza not in pizzas list")