from abc import ABC, abstractmethod
from project.core.validator import Validator
from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.validate_empty_string(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def add_fish(self, fish: BaseFish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__ != self.fish_type:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {self.fish_type} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_name = [f.name for f in self.fish]
        return f"{self.name}:\n" \
               f"Fish: {' '.join(fish_name) if fish_name else 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {sum(c.comfort for c in self.decorations)}"
