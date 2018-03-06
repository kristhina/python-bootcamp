class Product:
    """
    class Product says about energetic values for all the products that
    our User can use to prepare his dishes
    :type product_id : int autoincrement
    :type name : string
    :type calories : int
    :type protein : int
    :type fat : int
    :type carbohydrates : int
    :type list_of_dishes : list of Dish
    """

    def __init__(self, product_id, name, calories, protein, fat, carbohydrates):
        self.list_of_dishes = []
        self.carbohydrates = carbohydrates
        self.fat = fat
        self.protein = protein
        self.calories = calories
        self.name = name
        self.product_id = product_id

    def __str__(self):
        return "{}: {} kalorii, {} białka, {} tłuszczy, {} węglowodanów".\
            format(self.name, self.calories, self.protein, self.fat, self.carbohydrates)


class Ingredient:
    """
    class Ingredient says how much of product do we have to use to prepare our dish
    :type product : Product
    :type amount : float
    """
    def __init__(self, ingredient_id, amount, product):
        self.ingredient_id = ingredient_id
        self.product = product
        self.ingredient_amount = amount
        self.ingredient_calories = self.ingredient_amount * self.product.calories / 100
        self.ingredient_protein = self.ingredient_amount * self.product.protein / 100
        self.ingredient_fat = self.ingredient_amount * self.product.fat / 100
        self.ingredient_carbohydrates = self.ingredient_amount * self.product.carbohydrates / 100

    def __str__(self):
        return "{} g produktu {}".format(self.ingredient_amount, self.product.name)


class Dish:
    """
    class Dish is a list of products used to prepare that dish
    :type dish_id : int autoincrement
    :type name : str
    """
    def __init__(self, dish_id, name):
        self.name = name
        self.dish_id = dish_id
        self.list_of_ingredients = []

    def add_ingredient(self, ingredient):
        self.list_of_ingredients.append(ingredient)

    def __str__(self):
        a = [str(item) for item in self.list_of_ingredients]
        return "Potrawa: {} Lista składników: {}".format(self.name, a)

    def count_weight(self):
        amount = 0
        for ingredient in self.list_of_ingredients:
            amount += ingredient.ingredient_amount
        return amount

    def count_calories(self):
        calories = 0
        for ingredient in self.list_of_ingredients:
            calories += ingredient.ingredient_calories
        calories = calories*self.count_weight()/100
        return calories

    def count_fat(self):
        fat = 0
        for ingredient in self.list_of_ingredients:
            fat += ingredient.ingredient_fat
        fat = fat*self.count_weight()/100
        return fat

    def count_protein(self):
        protein = 0
        for ingredient in self.list_of_ingredients:
            protein += ingredient.ingredient_protein
        protein = protein * self.count_weight() / 100
        return protein

    def count_carbohydrates(self):
        carbohydrates = 0
        for ingredient in self.list_of_ingredients:
            carbohydrates += ingredient.ingredient_carbohydrates
        carbohydrates = carbohydrates * self.count_weight() / 100
        return carbohydrates


class Portion:
    """
    class Portion says about the amount of the dish that has been eaten by the User
    :type portion_id : int autoincrement
    :type portion_amount : int
    :type portion_dish : Dish

    """

    def __init__(self, portion_id, portion_amount, portion_dish):
        self.portion_dish = portion_dish
        self.portion_amount = portion_amount
        self.portion_id = portion_id

    def count_calories(self):
        return self.portion_dish.count_calories() * self.portion_amount

    def count_fat(self):
        return self.portion_dish.count_fat() * self.portion_amount

    def count_protein(self):
        return self.portion_dish.count_protein() * self.portion_amount

    def count_carbohydrates(self):
        return self.portion_dish.count_carbohydrates() * self.portion_amount

    def __str__(self):
        return "{} g potrawy {}".format(self.portion_amount, self.portion_dish.name)



class DailyMeals:
    """
    class DailyMeals is used to present the list of all the Portions of the Dish that had been
    eaten by the User during one day
    :type dailymeals_id : int autoincrement
    :type date : datetime
    :type user : User
    """
    def __init__(self, dailymeals_id, date, user):
        self.user = user
        self.date = date
        self.dailymeals_id = dailymeals_id
        self.list_of_meals = []

    def add_meal(self, meal_portion):
        """
        adds new Portion od the Dish to the list of Daily Meals eaten by the User
        :param meal_portion: Portion
        """
        self.list_of_meals.append(meal_portion)

    def __str__(self):
        a = [str(item) for item in self.list_of_meals]
        return "Lista potraw w dniu {}: {}".format(self.date, a)


class User:
    """
    class User
    :type id_user : int autoincrement
    :type name : str
    :type email : str
    :type weight : int
    :type height : int
    :type logged : bool
    :type password : str
    """

    def __init__(self, id_user, name, email, weight, height, logged, password):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.weight = weight
        self.height = height
        self.logged = logged
        self.password = password

    def log_user(self):
        pass

    def count_bmi(self):
        pass


marchew = Product(1, "marchew", 25, 2, 1, 15)
jablko = Product(2, "jabłko", 30, 3, 4, 17)
pomidor = Product(3, "pomidor", 15, 1, 1, 5)

ingr1 = Ingredient(1, 55, marchew)
ingr2 = Ingredient(2, 50, jablko)
ingr3 = Ingredient(3, 150, pomidor)

surowka = Dish(1, "surówka")
surowka.add_ingredient(ingr1)
surowka.add_ingredient(ingr2)

salatka_pomidor = Dish(2, "sałatka")
salatka_pomidor.add_ingredient(ingr3)

portion_of_surowka = Portion(1, 45, surowka)
portion_of_salatka = Portion(2, 150, salatka_pomidor)

krysia = User(1, "Krysia", "ja@gmial.ol", 45, 155, False, 'asdf')

meals_day_one = DailyMeals(1, "today", krysia)
meals_day_one.add_meal(portion_of_surowka)
meals_day_one.add_meal(portion_of_salatka)


print(marchew)
print(ingr1)
print(surowka)
print(surowka.count_weight())
print(portion_of_surowka)
print(meals_day_one)