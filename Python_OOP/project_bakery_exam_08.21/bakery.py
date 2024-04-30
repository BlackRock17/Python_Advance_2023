from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.core.validator import Validator


class Bakery:
    VALID_FOOD_TYPE = {
        "Bread": Bread,
        "Cake": Cake
    }
    VALID_DRINK_TYPE = {
        "Tea": Tea,
        "Water": Water
    }
    VALID_TABLE_TYPE = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_name(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if name in [m.name for m in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in self.VALID_FOOD_TYPE.keys():
            new_food = self.VALID_FOOD_TYPE[food_type](name, price)
            self.food_menu.append(new_food)
            return f"Added {new_food.name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in [m.name for m in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in self.VALID_DRINK_TYPE.keys():
            new_drink = self.VALID_DRINK_TYPE[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {new_drink.name} ({new_drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in self.VALID_TABLE_TYPE.keys():
            new_table = self.VALID_TABLE_TYPE[table_type](table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {new_table.table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = None
        for t in self.tables_repository:
            if not t.is_reserved and t.capacity >= number_of_people:
                table = t
                break
        else:
            return f"No available table for {number_of_people} people"

        table.is_reserved = True
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = self.__find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered = f"Table {table_number} ordered:\n"
        non_ordered = f"{self.name} does not have in the menu:\n"

        for name in args:
            for menu in self.food_menu:
                if menu.name == name:
                    ordered += repr(menu) + "\n"
                    table.food_orders.append(menu)
                    break
            else:
                non_ordered += name + "\n"

        return ordered.strip() + "\n" + non_ordered.strip()

    def order_drink(self, table_number: int, *args):
        table = self.__find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered = f"Table {table_number} ordered:\n"
        non_ordered = f"{self.name} does not have in the menu:\n"

        for name in args:
            for menu in self.drinks_menu:
                if menu.name == name:
                    ordered += repr(menu) + "\n"
                    table.drink_orders.append(menu)
                    break
            else:
                non_ordered += name + "\n"

        return ordered.strip() + "\n" + non_ordered.strip()

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        res = []
        for table in self.tables_repository:
            if not table.is_reserved:
                res.append(table.free_table_info())

        return "\n".join(res)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __find_table(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return table





