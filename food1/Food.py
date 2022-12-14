class Food:
    ingredients: []

    def name(self):
        pass


class FastFood(Food):
    def name(self):
        pass


class BurgerFood(FastFood):
    def name(self):
        return "Burger"


class PizzaFood(FastFood):
    def name(self):
        return "Pizza"


class FriedChickenFood(FastFood):
    def name(self):
        return "Fried Chicken"


class RestaurantFood(Food):
    def name(self):
        pass


class PastaFood(RestaurantFood):
    def name(self):
        return "Pasta"
