from project_shopping_cart_unittest.client import Client
from project_shopping_cart_unittest.meals.dessert import Dessert
from project_shopping_cart_unittest.meals.main_dish import MainDish
from project_shopping_cart_unittest.meals.meal import Meal
from project_shopping_cart_unittest.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __find_client(self, phone_num):
        for c in self.clients_list:
            if c.phone_number == phone_num:
                return c

    def __check_if_client_is_registered(self, phone_num):
        for c in self.clients_list:
            if c.phone_number == phone_num:
                return True

    def __validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def register_client(self, client_phone_number):
        if self.__check_if_client_is_registered(client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self):
        self.__validate_menu()

        result = [m.details() for m in self.menu]

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        self.__validate_menu()

        if not self.__check_if_client_is_registered(client_phone_number):
            self.register_client(client_phone_number)

        current_client = self.__find_client(client_phone_number)

        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in [m.name for m in self.menu]:
                raise Exception(f"{meal_name} is not on the menu!")
            current_meal = self.__find_meal(meal_name)
            if current_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {type(current_meal).__name__}: {meal_name}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            current_meal = self.__find_meal(meal_name)

            if meal_name not in current_client.ordered_quantity:
                current_client.ordered_quantity[meal_name] = 0

            current_client.ordered_quantity[meal_name] += quantity
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * quantity
            current_meal.quantity -= quantity

        meal_names = [n.name for n in current_client.shopping_cart]

        return f"Client {current_client.phone_number} successfully ordered {', '.join(meal_names)} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        current_client = self.__find_client(client_phone_number)
        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in current_client.ordered_quantity.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += quantity

        current_client.shopping_cart = []
        current_client.ordered_quantity = {}
        current_client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        current_client = self.__find_client(client_phone_number)
        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = current_client.bill
        current_client.shopping_cart = []
        current_client.ordered_quantity = {}
        current_client.bill = 0.0
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


