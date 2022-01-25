class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 1000)
print(DivisionByNull.divide_by_null(100, 0))
print(DivisionByNull.divide_by_null(100, 1))
print(div.divide_by_null(100, 0))
