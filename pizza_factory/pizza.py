class DoughFactory:
    def get_dough(self):
        return "insecticide treated wheat dough"

class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print("Getting Dough")
        print()
        print("Making pie with %s " % super().get_dough())
        print()
        for topping in toppings:
            print("Adding: %s" % topping)

if __name__ == '__main__':
    Pizza().order_pizza('pepperoni', 'Bell pepper', 'Mushrooms')

