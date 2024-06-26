from project_comp_store.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    MAX_RAM = 64

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if not self.valid_ram(ram) or ram > Laptop.MAX_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

