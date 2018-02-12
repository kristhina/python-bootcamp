class Product:
    """
    class Product says about energetic values for all the products that
    our User can use to prepare his dishes
    :type name : string
    :type calories : int
    :type protein : int
    :type fat : int
    :type carbohydrates : int
    :type list_of_dishes : list of Dish
    """

    def __init__(self, my_id, name, calories, protein, fat, carbohydrates):
        self.list_of_dishes = []
        self.carbohydrates = carbohydrates
        self.fat = fat
        self.protein = protein
        self.calories = calories
        self.name = name
        self.my_id = my_id


class Ingredient:
    """
    class Ingredient says how much of product do we have to use to prepare our dish
    :type product : Product
    :type amount : float
    """
    def __init__(self, amount, product):
        self.product = product
        self.amount = amount


class Dish:
    def __init__(self, dish_id):
        self.dish_id = dish_id
        self.list_of_ingredients = []

    def add_ingredient(self, ingredient):
        self.list_of_ingredients.append(ingredient)



class Portion:
    pass


class DailyMeals:
    pass


class User:
    pass


