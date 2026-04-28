class IntegerProcessor:
    def __init__(self):
        self.file_name = "integer_file_processor/integers.txt"
        self.double_file = "double.txt"
        self.triple_file = "triple.txt"

    def read_numbers(self):
        with open(self.file_name, "r") as file:
            return file.read().split()