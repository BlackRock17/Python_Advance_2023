class PizzaDelivery:

    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        elif quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

    def make_order(self):
        self.ordered = True
        i_q = [f"{key}: {value}"for key, value in self.ingredients.items()]

        return f"You've ordered pizza {self.name} prepared with {', '.join(i_q)} and the price will be {self.price}lv."
