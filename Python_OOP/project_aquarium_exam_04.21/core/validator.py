class Validator:

    @staticmethod
    def validate_empty_string(value, massage):
        if value == "":
            raise ValueError(massage)

    @staticmethod
    def validate_price(value, massage):
        if value <= 0:
            raise ValueError(massage)
