from project.bakery import Bakery

bakery = Bakery("Cool")

print(bakery.add_food("Bread", "nice_bread", 2))
print(bakery.add_food("Cake", "nice_cake", 5))

print(bakery.add_drink("Tea", "hot_tea", 200, "green"))
print(bakery.add_drink("Water", "water", 250, "hissar"))

print(bakery.add_table("InsideTable", 1, 3))
print(bakery.add_table("OutsideTable", 51, 4))
print(bakery.get_free_tables_info())

print(bakery.reserve_table(4))
print(bakery.reserve_table(3))

print(bakery.order_food(1, "nice_bread", "nice_cake", "choco"))
print(bakery.order_drink(1, "hot_tea", "wine"))


