def add_two_numbers(num1: int, num2: int) -> int:
    min_bound = 0
    max_bound = 100

    num1_in_range = min_bound <= num1 and num1 <= max_bound
    num2_in_range = min_bound <= num2 and num2 <= max_bound
    if num1_in_range and num2_in_range:
        return sum([num1, num2])
    raise ValueError(f"Inputs outisde of the range of {min_bound} - {max_bound}")


class SumSolution:
    def compute(self, x, y):
        return add_two_numbers(x, y)


