from pizza import Pizza, DoughFactory

class OrganicDoughFactory(DoughFactory):
    
    def get_dough(self):
        return 'pure untreated wheat dough'

class OrganicPizza(Pizza, OrganicDoughFactory):
    pass

if __name__ == "__main__":
    print(OrganicPizza.mro())
    OrganicPizza().order_pizza('sausage', 'Mushroo')
