class Operator:
    def __init__(self, operator_type) -> None:
        valid_operators = ["+", "-", "*", "/"]
        if operator_type not in valid_operators:
            raise ValueError(f"Unsupported operator: {operator_type}")
        self.type = operator_type

    def execute(self, first_value, second_value):
        

        if self.type == "+":
            return first_value + second_value
        elif self.type == "-":
            return first_value - second_value
        elif self.type == "*":
            return first_value * second_value
        elif self.type == "/":
            if second_value == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return first_value / second_value
