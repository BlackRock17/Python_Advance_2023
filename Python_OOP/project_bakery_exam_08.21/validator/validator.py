class Validator:

    @staticmethod
    def validate_name(value, massage):
        if value.strip() == "":
            raise ValueError(massage)

    @staticmethod
    def validate_positive_number(value, massage):
        if value <= 0:
            raise ValueError(massage)

    @staticmethod
    def validate_table_number(number, min_r, max_r, massage):
        if number < min_r or number > max_r:
            raise ValueError(massage)

