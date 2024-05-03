from project_comp_store.computer_types.desktop_computer import DesktopComputer
from project_comp_store.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)

        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)

        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for comp in self.warehouse:
            if comp.price <= client_budget and comp.processor == wanted_processor and comp.ram >= wanted_ram:
                self.profits += client_budget - comp.price
                self.warehouse.remove(comp)
                return f"{comp} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")

