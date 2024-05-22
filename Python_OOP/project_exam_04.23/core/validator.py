class Validator:

    @staticmethod
    def validate_name(name, massage):
        if name.strip() == "":
            raise ValueError(massage)

    @staticmethod
    def validate_rating(value, massage):
        if value < 0:
            raise ValueError(massage)

    @staticmethod
    def validate_length_of_route(route_len, massage):
        if route_len < 1:
            raise ValueError(massage)
