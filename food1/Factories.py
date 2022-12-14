from Food import Food, PastaFood, FastFood, BurgerFood, PizzaFood, FriedChickenFood, RestaurantFood


class FoodFactory:
    def produce(self):
        return Food()


class FastFoodFactory(FoodFactory):
    def produce(self):
        return FastFood()


class BurgerFactory(FastFoodFactory):
    def produce(self):
        return BurgerFood()


class PizzaFactory(FastFoodFactory):
    def produce(self):
        return PizzaFood()


class FriedChickenFactory(FastFoodFactory):
    def produce(self):
        return FriedChickenFood()


class RestaurantFoodFactory(FoodFactory):
    def produce(self):
        return RestaurantFood()


class PastaFactory(RestaurantFoodFactory):
    def produce(self):
        return PastaFood()


factoryList = []
foodList = []

factoryList.append(BurgerFactory())
factoryList.append(PizzaFactory())
factoryList.append(FriedChickenFactory())
factoryList.append(PastaFactory())

for factory in factoryList:
    foodList.append(factory.produce())

for food in foodList:
    print(food.name())

# Run:
# python food1/Factories.py