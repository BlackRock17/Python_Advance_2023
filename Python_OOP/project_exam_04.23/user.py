from project.core.validator import Validator


class User:

    def __init__(self, first_name, last_name, driving_license_number):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        self.is_blocked = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        Validator.validate_name(value, "First name cannot be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        Validator.validate_name(value, "Last name cannot be empty!")
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        Validator.validate_name(value, "Driving license number is required!")
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        Validator.validate_rating(value, "Users rating cannot be negative!")
        self.__rating = value

    def increase_rating(self):
        self.rating += 0.5
        if self.rating > 10:
            self.rating = 10

    def decrease_rating(self):
        if self.rating - 2 < 0:
            self.rating = 0
            self.is_blocked = True
        else:
            self.rating -= 2

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"


