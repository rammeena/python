#better_pizza.py

from pizza import DoughFactory, Pizza

class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return "pure untreated wheat dough"

class OrganicPizza(Pizza, OrganicDoughFactory):
    pass

if __name__ == '__main__':
    OrganicPizza().order_pizza('pepperoni', 'Bell pepper', 'Mushrooms')

