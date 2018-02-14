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

    def __str__(self):
        return "{}: {} kalorii, {} białka, {} tłuszczy, {} węglowodanów".\
            format(self.name, self.calories, self.protein, self.fat, self.carbohydrates)


class Ingredient:
    """
    class Ingredient says how much of product do we have to use to prepare our dish
    :type product : Product
    :type amount : float
    """
    def __init__(self, amount, product):
        self.product = product
        self.ingredient_amount = amount
        self.ingredient_calories = self.ingredient_amount * self.product.calories / 100
        self.ingredient_protein = self.ingredient_amount * self.product.protein / 100
        self.ingredient_fat = self.ingredient_amount * self.product.fat / 100
        self.ingredient_carbohydrates = self.ingredient_amount * self.product.carbohydrates / 100

    def __str__(self):
        return "{} g produktu {}".format(self.ingredient_amount, self.product.name)



class Dish:
    def __init__(self, dish_id):
        self.dish_id = dish_id
        self.list_of_ingredients = []

    def add_ingredient(self, ingredient):
        self.list_of_ingredients.append(ingredient)

    def __str__(self):
        a = [str(item) for item in self.list_of_ingredients]
        return "Lista składników: {}".format(a)

    def count_weight(self):
        amount = 0
        for ingredient in self.list_of_ingredients:
            amount += ingredient.ingredient_amount
        return amount

    def count_calories(self):
        calories = 0
        for ingredient in self.list_of_ingredients:
            calories += ingredient.ingredient_calories
        return calories

    def count_fat(self):
        fat = 0
        for ingredient in self.list_of_ingredients:
            fat += ingredient.ingredient_fat
        return fat

    def count_protein(self):
        protein = 0
        for ingredient in self.list_of_ingredients:
            protein += ingredient.ingredient_protein
        return protein



class Portion:
    pass


class DailyMeals:
    pass


class User:
    pass


marchew = Product(1, "marchew", 25, 2, 1, 15)
jablko = Product(2, "jabłko", 30, 3, 4, 17)

ingr1 = Ingredient(55, marchew)
ingr2 = Ingredient(50, jablko)

surowka = Dish(1)
surowka.add_ingredient(ingr1)
surowka.add_ingredient(ingr2)

print(marchew)
print(ingr1)
print(surowka)
print(surowka.count_weight())